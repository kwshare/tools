#!/usr/bin/python
# coding:utf-8

# display query page


from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/<username>')
def hello(username):
    return read(username)


@app.route('/')
def index():
    return read()


def read(user=None):
    con = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='sign')

    if user:
        cur = con.cursor()
        cur.execute('select * from sign WHERE NAME =%s', (user,))
        data = cur.fetchall()

        if len(data) == 0:
            return 'No result has been found...'
        display = ''
        for i in range(len(data)):
            display = display + str(data[i][0]) + ' ' + data[i][1] + ' ' + str(data[i][2]) + '<br>'
        return display

    else:
        cur = con.cursor()
        cur.execute('select * from sign')
        data = cur.fetchall()
        display = ''
        for i in range(len(data)):
            display = display + str(data[i][0]) + ' ' + data[i][1] + ' ' + str(data[i][2]) + '<br>'
        return display


if __name__ == '__main__':
    app.run(debug=True)
