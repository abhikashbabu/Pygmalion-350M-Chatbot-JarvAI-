# Project Name: JarvAI - AI Chatbot using Pygmalion-350M
## Overview
JarvAI is an AI-powered chatbot built using the Pygmalion-350M language model. It is a simple Flask-based API that allows users to interact with the chatbot via HTTP requests.

## Features
- Natural language conversation with AI.
- Lightweight and fast using Pygmalion-350M model.
- REST API interface for easy integration into websites and apps.
## Requirements
- Python 3.8+
- Transformers library
- Flask library
- Install dependencies using:
- pip install transformers flask torch


## Model Used
- Pygmalion-350M from Hugging Face.
- Model URL: https://huggingface.co/PygmalionAI/pygmalion-350m

## Setup & Installation

- Clone the repository or create a project folder.
- Create a Python file (e.g., app.py) and add the following code:

```sh
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("PygmalionAI/pygmalion-350m")
model = AutoModelForCausalLM.from_pretrained("PygmalionAI/pygmalion-350m").to("cpu")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    
    if not user_input:
        return jsonify({"error": "Message cannot be empty"}), 400

    inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True).to("cpu")
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=150,
        pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

```

Run the application:

```sh
python app.py
```
The server will start at http://localhost:5000.


## Deployment
- Locally
- Simply run the Flask app with:
```sh
python app.py
```
- On a Cloud Platform (Optional)
- Deploy on platforms like Heroku, Render, or AWS EC2 for public access.

# Notes
Ensure your system has sufficient RAM and CPU for smooth performance.
For production, consider using GPU or cloud computing for better efficiency.


# Future Scope:
- Speech-to-Text Integration for voice commands.
- Text-to-Speech Output for Jarvis-like audio responses.
- API-based GPT Model Support for advanced responses.
- User Authentication to personalize chat experiences.

## Plugins

Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Transformers library | https://huggingface.co/docs/transformers/index |
| Flask library| https://pypi.org/project/Flask/ |

## Contact
For queries or issues, reach out at info@appsredx.com , abhikashbabu@gmail.com .

## License
MIT
