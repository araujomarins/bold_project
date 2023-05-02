# Who the API Works

The API uses OPENAI API to generate a list of keywords that represents the scholarship description. In the query to create this list, there are some restrictions on the output such as:

- Split the keywords;
- Restrict the number of keywords with an upper bound;
- Remove personal names; and
- Add professions and jobs mentioned.

After retrieving this list, we do some post-processing (mainly using the [spacy package](https://spacy.io/api)):

- Remove keywords that represent locations in general (countries, states, and cities);
- Remove keywords according to a blacklist of words;
- Remove verbs, adjectives, and pronouns.

After that, we go to the image generation. We are using the keywords to search the internet for images that can represent it. We are using [Unsplash API](https://unsplash.com/documentation) to do it.

The last step is to create the image according to the requirements specified:

- Size: 1360x1020;
- Output: Base64 image; and
- Save as PNG.

On top of that, we are adding the scholarship title to the image.
# Setup

1. Create the environment and activate it:
   
   `conda env create -f environment.yml` -> `source activate bold-project`

2. Start the server with the API endpoint:
   
    `python image_generation_app.py`

3. Do a request. There is a python file that does a request to the API endpoint ("test_api.py"):
   
   `python test_api.py  `
# Examples

This examples is based on [a scholarship announced on Bold website](https://bold.org/scholarships/be-the-change-essay-scholarship/). The cover image generated for this is below:

<p align="center" width="100%">
    <img width="75%" src="assets/examples/example1_image.png"> 
</p>

Another examples is based on [this scholarship](https://bold.org/scholarships/cardel-love-scholarship/). The cover image generated for this is below:

<p align="center" width="100%">
    <img width="75%" src="assets/examples/example2_image.png"> 
</p>

It is worth noting that the API is built on top of OpenAI's API, which does not guarantee the same output for the same input. So, when running the API, one can get different results for the same input.
# Output

The output of the API is a JSON with only one key: "image_base64", and the value is a base64 encoded image.
# Next Improvements

## The approach
The current API works on a keyword-based approach, which works well but has some disadvantages, such as the need 
of establishing post-processing steps. The current steps are scalable in most cases, but when we need to define 
the BLACKLIST_KEYWORDS variable, it does not scale well. With proper time, probably we will converge to a final list, but it will take some time and experience with the problem.

## Title Writing on Top of the Image

The current approach has some disadvantages, such as:

- The title box can hide important artifacts of the image, which can confuse.
- The font is not customizable

The approach I suggest is to do in the front end, rendering the image and the box with the text, and then, give 
the user the ability to drag the box around and choose the best location to anchor it.

## Feedback Loop

A feedback loop can be implemented in the current version already. The API can retrieve more than one image, and this can be delivered to the user in order until the donor is satisfied. If the donor is not satisfied with any of the images, a new request can be done with a higher temperature.

This process of retrieving the quality of predictions can be used for the following versions of the model, as we will have access to a labeled dataset. 

## Fine-tunning

Using past data from already created scholarships alongside the labels mentioned in the previous section can be used to create a fine-tuned model. 

## Legal Issues?

The current approach uses images available on the internet. If this creates any sort of legal issues, it is possible to generate images closer to the one used using OPENAI's API.
