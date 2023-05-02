from flask import Flask, request, jsonify

from src.image_processing import generate_cover_image

app = Flask(__name__)
print(app)
@app.route('/bold_ai_kw2img', methods=['POST'])
def generate_image():
    text_input = request.get_json()
    output = generate_cover_image(text_input)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)