#coding=utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    # 注意端口被占用
    app.run(host='127.0.0.1', port=9090, debug=True)
