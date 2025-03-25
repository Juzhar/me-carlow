# -*- coding: utf-8 -*-
"""
HW7
"""
# Q5

from flask import Flask, request
import pandas as pd
import random as rnd

poke = pd.read_csv("../Data/pokemon.csv")

app = Flask(__name__)
log = []

team = []
@app.route('/create', methods=['POST'])
def generate():
    if len(team) != 0:
        return "team already exists"
    else:
        rand_ints = []
        for i in range(6):
            number = rnd.randint(1, 1305)
            if number not in rand_ints:
                rand_ints.append(number)
        for number in rand_ints:
            for index, row in poke.iterrows():
                if index == number:
                    team.append(row['identifier'])
                    log.append("Action " + str(request.method) + " "+ row['identifier'] + " added")
        with open("out.log", "w") as file:
            for action in log:
                file.write(action)
                file.write('\n')
        return "team created successfully"
@app.route('/list', methods=['GET'])
def list_pokemon():
    for pokemon in team:
        log.append("Action " + str(request.method) +" "+ pokemon + " listed")
    with open("out.log", "w") as file:
        with open("out.log", "w") as file:
            for action in log:
                file.write(action)
                file.write('\n')
    return team
@app.route('/delete', methods=['DELETE'])
def delete():
    for pokemon in team:
        log.append("Action " + str(request.method) +" "+ pokemon + " deleted")
    team.clear()
    with open("out.log", "w") as file:
        with open("out.log", "w") as file:
            for action in log:
                file.write(action)
                file.write('\n')
    return "team deleted successfully"
app.run(host='127.0.0.1', port=8989)