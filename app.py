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
    url = "https://www.hcs.co.jp/news/docs/test.pdf"
    
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

#GET,POST TEST
@app.route('/test', methods=['GET', 'POST'])
def test():
    try:
        if request.method == 'GET':
            return request.args.get('query', '')
        elif request.method == 'POST':
            return request.form['query']
        else:
            return abort(400)
    except Exception as e:
        return str(e)









