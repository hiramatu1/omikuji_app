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
    html = '''
    <form action="/test">
        <p><label>test: </label>
        <input type="text" name="query" value="default">
        <button type="submit" formmethod="get">GET</button>
        <button type="submit" formmethod="post">POST</button></p>
    </form>
    '''
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run()









