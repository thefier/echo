import os, json
from flask import Flask, request, jsonify, render_template, abort
import openai
from utils import process_echo

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
API_TOKEN = os.getenv("API_TOKEN", "change-me")

@app.before_request
def auth():
    if request.endpoint not in ('index', 'static'):
        token = request.headers.get("Authorization", "")
        if token != f"Bearer {API_TOKEN}":
            abort(401)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save uploaded file
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", file.filename)
    file.save(filepath)

    # Process echo
    echo_result = process_echo(filepath)

    # Prompt OpenAI
    prompt = f"Given this echocardiographic data: {echo_result}, generate a concise clinical summary."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    report = response.choices[0].message.content

    return jsonify({"echo_result": echo_result, "report": report})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
