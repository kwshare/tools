#coding:utf-8
from flask import Flask,send_file,send_from_directory

app=Flask(__name__)


@app.route('/')
def m():
    # return '''<button onclick="javascript:window.location.href='https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/logo_white_fe6da1ec.png'">Copy Text</button>
    # '''
    return send_file('2.zip')

if __name__ == '__main__':
    app.run(debug=True)