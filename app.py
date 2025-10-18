from flask import Flask, render_template
import random
from io import BytesIO
from urllib import request
from pdfminer.high_level import extract_text

app = Flask(__name__)

omikuji_results = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']

# おみくじを引く画面へ遷移
@app.route('/')
def index():
    print("hello1")
    return render_template('index.html')

# おみくじの結果をランダムで選択し、結果画面へ遷移
@app.route('/omikuji')
def omikuji():
    result = random.choice(omikuji_results)
    return render_template('result.html', result=result)

if __name__ == '__main__':

    app.run(debug=True)



