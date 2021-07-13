from logging import debug
from re import S
from flask import Flask,render_template,request
# from flask.wrappers import request
app=Flask(__name__)
import nltk


@app.route('/')
def para_input():
    return render_template('base-1.html')

@app.route('/para_description',methods=['POST'])
def para_details():
    a=request.form.get('text')
    words=str(len(nltk.word_tokenize(a)))
    sentences=str(len(nltk.sent_tokenize(a)))

    x=f"number of words = {words}. number of sen = {sentences}."
    return x

    # number of words , number of sen , keyword density

app.run(debug=True)