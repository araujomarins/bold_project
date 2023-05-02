import openai
import os

from src.image_processing import generate_cover_image

# set up OpenAI API credentials
openai.api_key = os.environ.get('OPENAI_API_KEY')

# define the text to analyze
text = """Cardel Love was a beloved basketball player from Buffalo, New York who passed away in 2005. 

Cardel lived his life with joy, charisma, and a love for his community, school, and family. 

This scholarship seeks to honor Cardel’s life and legacy by supporting first-generation, BIPOC students from New York so they can pursue higher education.

Any BIPOC high school senior from New York who will be a first-generation college student may apply for this scholarship. 

To apply, tell us about yourself and what you hope to study and achieve in college."""

# text = """
# Major La-Goge W. Graham had committed his life to serving others through his military, ministry and teaching career. He was well-loved and respected by his students and always found a way to give back to his community.

# Major “Go” Graham devoted years of his life organizing parades, planning “Weekend in the Woods” with his cadets, food banks for veterans, and students, serving his community through the agape love of Christ, while he and his wife fostered many children in need of a safe home. But his true passion was teaching his students about the privilege of being able to serve others.

# After a hard-fought battle with cancer, he passed away on January 5th, 2021. His legacy and mission to serve the community can continue by inspiring future generations to give back to their community through this scholarship.

# This scholarship seeks to honor Major La-Goge W. Graham and support graduating JROTC cadets or undergraduates in ROTC programs in the United States.

# Any high school junior or senior in JROTC or ROTC may apply for this scholarship.

# To apply, tell us how you plan to make a difference in the world with your armed forces career.
# """

# text = """
# Novitas believes that diversity is critical to the public relations industry.

# It is important to encourage increasingly diverse voices in all fields, but the efforts to promote diversity in public relations are valuable to creating a more educated, accepting communications industry and society. The Novitas Diverse Voices Scholarship will support a student who is interested in pursuing a career in public relations and who comes from a background that remains underrepresented in the field. 

# High school seniors or undergraduate students are eligible to apply if they are an underrepresented minority, including but not limited to, low-income backgrounds, first generation college students, BIPOC or from the LGBTQIA+ community. Students applying must be pursuing a career in public relations, although it is not required to be majoring in public relations or communications.

# To apply, please write about what impact the power of diverse voices in public relations can have on shaping the public narrative.
# """

# text = """
# Paying it forward is extremely important in regard to seeing the change you want to see in the world. 

# There are more than one hundred Historically Black Colleges and Universities in the United States that have the power to change the lives of the thousands of students that walk their halls. At these schools, students from all backgrounds are able to expand their knowledge, pursue their dreams, and be the change they want to see in the world.

# This scholarship seeks to support students who are attending HBCUs so that they can achieve their dreams of higher education.

# Any undergraduate student attending an HBCU who has at least a 3.3 GPA and has community service or leadership experience may apply for this scholarship.

# To apply, submit a 750-1,000-word essay telling us about how your experience giving back/serving has shaped your perspective on humanity and how these experiences affected your career choice and future goals.
# """

scholarship_object = {
    "title": "Cardel Love Scholarship",
    "description": text,
    "award_ammount": 1000,
    "n_winners": 2,
}

mode = "keyword"
image_size = (1360, 1020)
n_images = 5

generate_cover_image(
    scholarship_object=scholarship_object,
    image_size=image_size,
    n_images=n_images,
    mode=mode,
)