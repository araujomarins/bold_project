import requests

text = """
Paying it forward is extremely important in regard to seeing the change you want to see in the world. 

There are more than one hundred Historically Black Colleges and Universities in the United States that have the power to change the lives of the thousands of students that walk their halls. At these schools, students from all backgrounds are able to expand their knowledge, pursue their dreams, and be the change they want to see in the world.

This scholarship seeks to support students who are attending HBCUs so that they can achieve their dreams of higher education.

Any undergraduate student attending an HBCU who has at least a 3.3 GPA and has community service or leadership experience may apply for this scholarship.

To apply, submit a 750-1,000-word essay telling us about how your experience giving back/serving has shaped your perspective on humanity and how these experiences affected your career choice and future goals.
"""

scholarship_object = {
    "title": "'Be the Change' Essay Scholarship",
    "description": text,
    "award_ammount": 1000,
    "n_winners": 2,
}

# input_dict = {'title': 'Hello', 'description': ' World!'}
response = requests.post('http://localhost:5000/bold_ai_kw2img', json=scholarship_object)
print(response)
output_dict = response.json()

print(output_dict)  # {'result': 'Hello World!'}
