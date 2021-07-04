from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        data = json.dumps({
            'username': username,
            'password': password
        })
        return data

    else:
        data = '缺少参数'
        return data


@app.route('/post_login', methods=['POST'])
def post_login():
    method = request.method
    if method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        data = json.dumps({
            'username': username,
            'password': password
        })
        return data
    else:
        data = '缺少参数'
        return data


if __name__ == '__main__':
    app.run(host='0.0.0.0')
