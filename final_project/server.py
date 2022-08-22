"""
Server implimentation
"""

from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """
    Server implimentation of English to French
    """
    textToTranslate = request.args.get('textToTranslate')
    translated_text_to_french = translator.englishToFrench(textToTranslate)
    return translated_text_to_french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    Server ijmplimentation of French to English
    """
    textToTranslate = request.args.get('textToTranslate')
    translated_text_to_english = translator.frenchToEnglish(textToTranslate)
    return translated_text_to_english

@app.route("/")
def renderIndexPage():
    """
    Server implimentation of index rendering
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
