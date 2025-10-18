from flask import Flask, render_template
import random
from io import BytesIO
from urllib import request
from pdfminer.high_level import extract_text
import requests


@app.route('/', methods=['GET'])
def Hello():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def view():
    input_data = request.args.get('item')
    return render_template('index.html', item = input_data)






