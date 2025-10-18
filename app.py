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
    url = "https://www.jitec.ipa.go.jp/1_00topic/topic_20071225_shinseido_4.pdf"
    
    with request.urlopen(url) as res:
        f = BytesIO(res.read())
        text = extract_text(f)
        print(text[:300])
    print("hello2")
    return render_template('index.html')

# おみくじの結果をランダムで選択し、結果画面へ遷移
@app.route('/omikuji')
def omikuji():
    result = random.choice(omikuji_results)
    return render_template('result.html', result=result)

if __name__ == '__main__':

    app.run(debug=True)







