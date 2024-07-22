from flask import Flask, request, render_template, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate_text', methods=['POST'])
def translate_text():
    text = request.form['text']
    target_language = request.form['target_language']
    translation = translator.translate(text, dest=target_language)
    return jsonify(translation=translation.text)

if __name__ == '__main__':
    app.run(debug=True)
