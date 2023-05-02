import openai
import os
import spacy

import requests
import json
from typing import Tuple, List, Dict
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

from matplotlib import font_manager
import base64
import io

from .definition import QUERY_TEMPLATES, BLACKLIST_KEYWORDS
from .utils import clean_list, is_personal_name_or_city_name

UNSPLASH_ACCESS_KEY = "aXY6PcITRdYcqOhIM54JnH5JVQlTkJRcoIf4KkKqi3U"

# set up OpenAI API credentials
openai.api_key = os.environ.get('OPENAI_API_KEY')

nlp = spacy.load('en_core_web_sm')

def generate_cover_image(
        scholarship_object: Dict, 
        image_size: Tuple[int, int] = (1360, 1020),
        n_images: int = 5,
        mode: str = "keyword",
        ) -> Dict:
    """
    Generate a cover image for a scholarship object using OpenAI to extract keywords or a summary 
    from its description, and searching for relevant images online.

    Args:
        scholarship_object (Dict): A dictionary containing information about the scholarship, including its title and description.
        image_size (Tuple[int, int]): The size of the image to search for online. Defaults to (1360, 1020).
        n_images (int): The number of images to search for and choose from. Defaults to 5.
        mode (str): The mode used to generate the image query, either "keyword" or "summary". Defaults to "keyword".

    Returns:
        A dictionary containing the encoded image that describes the input text in base64 format.
    """
    # use OpenAI to extract keywords from the text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=QUERY_TEMPLATES[mode].format(scholarship_object["description"]),
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=.65,
    )

    if mode == "keyword":

        raw_keyowrds_list = response.choices[0].text[1:].split(", ")
        formated_keyowrds_list = clean_list(raw_keyowrds_list)
        
        keywords_list = [kw for kw in formated_keyowrds_list if not is_personal_name_or_city_name(kw)]
        kws_list = [kw for kw in keywords_list if kw not in BLACKLIST_KEYWORDS]

        filtered_words = []
        pos_to_exclude = ["VERB", "ADJ", "PROPN"]

        for word in kws_list:
            doc = nlp(word)
            if not any(token.pos_ in pos_to_exclude for token in doc):
                filtered_words.append(word)

        image_query = f"""
        {' '.join(filtered_words)}
        """

    elif mode == "summary":
        output = response.choices[0].text[1:]

        start_index = output.find("{")
        end_index = output.find("}") + 1

        # Extract the JSON string
        json_string = output[start_index:end_index]
        output_dict = json.loads(json_string)
        image_query = f"""
        scholarship {output_dict['Target']} {output_dict['Area']}
        """

    # print(image_query)

    images, image_urls = search_images(
        query=image_query,
        image_size=image_size,
        per_page=n_images,
    )

    image = images[0]

    image = add_description_to_image(image=image, text=scholarship_object["title"])

    # Convert the image to a binary format in memory
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        binary_data = output.getvalue()

    # Encode the binary data as base64
    encoded_image = base64.b64encode(binary_data).decode("utf-8")
    # Save the modified image
    # image.save('assets/examples/example1_image.png', format='PNG')
    image.save('image.png', format='PNG')

    return {"image_base64": encoded_image}

def add_description_to_image(image: Image.Image, text: str, box_color: str = "#1a035a") -> Image.Image:
    """
    Adds a box with a title on top of an image.

    Args:
        image (PIL.Image.Image): The image to add the box to.
        text (str): The text to add.
        box_color (str): The color of the box to draw behind the text, in the format `#RRGGBB`.

    Returns:
        PIL.Image.Image: The original image with the title writen.
    """
    width, height = image.size
    box_x1, box_y1 = int(0.05*width), int(0.7*height)
    box_x2, box_y2 = int(0.9*width), int(0.9*height)
    text_color = (255, 255, 255)

    # Create a drawing object
    draw = ImageDraw.Draw(image)
    # font = ImageFont.load_default()

    font = font_manager.FontProperties(family='sans-serif', weight='bold')
    font_file = font_manager.findfont(font)

    font = ImageFont.truetype(font_file, 50)

    draw.rectangle((box_x1, box_y1, box_x2, box_y2), width=0, fill=box_color)
    draw.text((int(0.1*width), int(0.75*height)), text, font=font, fill=text_color)

    return image

def search_images(query: str, image_size: Tuple[int, int], orientation: str = "landscape", per_page: int = 5) -> Tuple[List, List]:
    """Searches for images using the Unsplash API and retrieves a specified number of images.

    Args:
        query: A string containing the search query for the images.
        image_size: A tuple containing the desired width and height of the images.
        orientation: A string indicating the desired orientation of the images ("landscape", "portrait", or "squarish").
        per_page: An integer indicating the number of images to retrieve.

    Returns:
        A tuple containing a list of PIL Image objects and a list of image URLs retrieved from the Unsplash API.
    """
    orientation = "landscape"  # the desired image orientation
    per_page = 1  # the number of images to retrieve per page

    # API endpoint URL
    url = f"https://api.unsplash.com/search/photos?query={query}&orientation={orientation}&per_page={per_page}"
    # url = f"https://api.pexels.com/v1/search?query={image_query_by_area}&orientation={orientation}&per_page={per_page}"

    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    response = requests.get(url, headers=headers)
    # get the image URL from the API response
    image_urls = [response.json()["results"][i]["urls"]["regular"] for i in range(per_page)]

    image_data = [requests.get(url).content for url in image_urls]
    images = [Image.open(BytesIO(data)) for data in image_data]
    images = [image.resize(image_size) for image in images]

    return images, image_urls
