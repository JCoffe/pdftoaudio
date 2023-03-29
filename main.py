import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, Response
import time
from PyPDF2 import PdfReader
import requests
from gtts import gTTS




#TODO Load pdf file

#reader = PdfReader("pdf/pcl.pdf")
#TODO Get text from pdf
#page = reader.pages[0]
#print(page.extract_text())
#from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

#db = SQLAlchemy()

app = Flask(__name__)

##Connect to Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todos.db')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db.init_app(app)

#TODO API text to speech


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/convert", methods=['GET', 'POST'])
def convert():
    if request.method =='POST':
        reader = PdfReader("pdf/" + request.form['filepath'])
        page = reader.pages[0]
        text = page.extract_text()
        content = text[500:1500]
        language = "en"
        myobj = gTTS(text=content, lang=language, slow=False)
        myobj.save("sound/test.mp3")

    return render_template('index.html', text=text[:100])





if __name__ == '__main__':
    app.run(debug=True)
