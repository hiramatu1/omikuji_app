from flask import Flask, render_template, request
import random
from io import BytesIO
from urllib import request as librequest
from pdfminer.high_level import extract_text

app = Flask(__name__)

omikuji_results = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']

# おみくじを引く画面へ遷移
@app.route('/')
def index():
    return render_template('index.html')

# おみくじの結果をランダムで選択し、結果画面へ遷移
@app.route('/omikuji', methods=['GET', 'POST'])
def omikuji():
    try:
        if request.method == 'GET':
            print("1")
            input_data = request.args.get('query')
            print(input_data)
            return render_template('result.html', query=input_data)
        elif request.method == 'POST':
            print("2")
            return request.form['query']
        else:
            return abort(400)
    except Exception as e:
        return str(e)    

@app.route('/test', methods=['GET', 'POST'])
def test():
    try:
        if request.method == 'GET':
            print("1")
            input_data = request.args.get('query')
            print(input_data)
            return request.args.get('query', '')
        elif request.method == 'POST':
            print("2")
            return request.form['query']
        else:
            return abort(400)
    except Exception as e:
        return str(e)

@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('testapp/sampleform.html')
    if request.method == 'POST':
        print('POSTデータ受け取ったので処理します。')
        req1 = request.form['data1']
        return f'POST受け取ったよ: {req1}'

if __name__ == '__main__':
    app.run(debug=True)








