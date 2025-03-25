# -*- coding: utf-8 -*-
"""
HW7
"""
# Q4

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'Hello, Computer!'
    elif request.method == 'GET':
        return 'Hello, User!'
app.run(host='127.0.0.1', port=4356)
