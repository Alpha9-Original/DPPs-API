from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to call this API

# 🔐 Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyBN1nTlaaoq2vnIJ3fmhrD4BNVqnLzpQfY")

@app.route('/generate_dpp', methods=['POST'])
def generate_dpp():
    data = request.json

    subject = data['subject']
    class_level = data['class']
    num_questions = data['num_questions']
    difficulty = data['difficulty']
    topic = data['topic']

    prompt = f"""
    Generate a set of DPPs (Daily Practice Problems) for the subject: {subject}, 
    with {num_questions} questions, at {difficulty} difficulty level, focusing on the topic: {topic}. 
    Please ensure the problems are diverse and cover various aspects of the topic. 
    Also provide the answer key at the end with simple explanations.
    """

    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(
        prompt,
        generation_config={"max_output_tokens": 2000}
    )

    return jsonify({"dpp": response.text})


# ✅ Add this to actually run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
