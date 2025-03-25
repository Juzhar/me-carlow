# -*- coding: utf-8 -*-
"""
HW7
"""
# Q1

from flask import Flask
import pandas as pd
import random as rnd

poke = pd.read_csv("../Data/pokemon.csv")

app = Flask(__name__)

@app.route('/')
def index():
    number = rnd.randint(1, 1305)
    for index, row in poke.iterrows():
        if index == number:
            pokemon = row["identifier"]
    return "Hello " + str(pokemon)
app.run(host='127.0.0.1', port=4356)