from flask import Flask, request, jsonify, render_template
import openai
import os

# Initialize Flask app and OpenAI API credentials
app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"] = "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"
print(os.environ["OPENAI_API_KEY"])

# Define default route with GET method
@app.route("/")
def index():
    # Render index.html template
    return render_template("index.html")

# Define /prompt route with POST method
@app.route("/prompt", methods=["POST"])
def prompt():
    # Get input string from request data
    input_string = request.json["input_string"]

    # Generate response using OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_string,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Return response as JSON object
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run()