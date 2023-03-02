import os
import openai
import json
import openpyxl
from flask import Flask, request, render_template, jsonify

openai.api_key_path = "apikey.txt"

app = Flask(__name__,template_folder='templates')

@app.route('/', methods =["GET", "POST"])
def index():
  if request.method == "POST":
    prompt = request.form['prompt']
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0.48,
    max_tokens=1000,
    top_p=0.75,
    frequency_penalty=0.21,
    presence_penalty=0
    )
    s1 = json.dumps(response)
    json_object = json.loads(s1)
    output=""
    for each in json_object['choices']:
      x=each['text']
      output=x
    return jsonify({'output':output})
  return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


