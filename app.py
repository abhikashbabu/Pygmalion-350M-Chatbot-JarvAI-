from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("PygmalionAI/pygmalion-350m")
model = AutoModelForCausalLM.from_pretrained("PygmalionAI/pygmalion-350m").to("cpu")  # Agar server pe GPU ho to 'cuda' likhna

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True).to("cpu")
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[:, inputs["input_ids"].shape[-1]:][0], skip_special_tokens=True)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
