'''
Author: sunjie
Date: 2025-03-10 22:52:01
LastEditors: sunj
LastEditTime: 2025-03-11 22:27:48
FilePath: /sunjPy/wDemos/flaskDemo.py
'''

from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html", hero="sunjie")


@app.route("/choujiang")
def choujiang000():
    num = randint(1, 100)
    return render_template("index.html", hero="sunjie", num=num)
