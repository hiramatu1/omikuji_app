from flask import Flask, render_template
import random

app = Flask(__name__)

omikuji_results = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']

# おみくじを引く画面へ遷移
@app.route('/')
def index():
    return render_template('index.html')

# おみくじの結果をランダムで選択し、結果画面へ遷移
@app.route('/omikuji')
def omikuji():
    result = random.choice(omikuji_results)
    return render_template('result.html', result=result)

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
        
if __name__ == '__main__':
    app.run(debug=True)


