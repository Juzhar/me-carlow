# -*- coding: utf-8 -*-
"""
Final Project
"""
# API

from flask import Flask, request, jsonify
import sqlite3
import logging
import logging.config
import random as rnd 

logging.config.fileConfig('config.ini')
app = Flask(__name__)
logger = logging.getLogger(__name__)
db_path = "teambattle.db"
poke_params = ['ID', 'Name', 'Height', 'Weight', 'Experience']
trainer_params = ['Name', 'Email', 'Phone']
team_params = [ 'Name', 'Manager']
membership_params = ['PokemonID', 'TeamID']
battle_params = ['team1', 'team2']
trainer_id_list = []
team_id_list = []
team_count_list = []
teams_data = []
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT TeamID from membership")
rows = c.fetchall()
for row in rows:
    team_count_list.append(row[0])
conn.commit()
conn.close()
@app.route('/pokemon', methods=['POST', 'GET'])
def pokemon():
    data = request.get_json()
    if request.method == 'POST':
        for param in poke_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        Height = data.get('Height')
        Weight = data.get('Weight')
        Experience = data.get('Experience')
        poke_data = "INSERT INTO pokemon(ID, Name, Height, Weight, Experience) VALUES(" + str(ID) + ", '" + Name + "', " + str(Height) + ", " + str(Weight) + ", " + str(Experience) + ");"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(poke_data)
        conn.commit()
        conn.close()
        id_dict = {"Message":"Pokemon was successfully created"}
        return jsonify(id_dict)
    elif request.method == 'GET':
        if data.get('ID') != None:
            ID = data.get('ID')
            get_poke_data = "SELECT * FROM pokemon WHERE ID =" + str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_poke_data)
                row = c.fetchone()
                conn.close()
                id_dict = {"Pokemon":row}
                return jsonify(id_dict)
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
        elif data.get('Name') != None:
            Name = data.get('Name')
            get_poke_data = "SELECT * FROM pokemon WHERE Name ='" + Name + "';"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_poke_data)
                row = c.fetchone()
                conn.close()
                id_dict = {"Pokemon":row}
                return jsonify(id_dict)
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
        else:
            logger.error("An error ocurred")
            return "Error: Invalid ID", 500
        
@app.route('/trainer', methods=['POST', 'GET', 'DELETE'])
def trainer():
    data = request.get_json()
    if request.method == 'POST':
        for param in trainer_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        id_found = False
        while id_found == False:
            new_id = rnd.randint(1, 999)
            if new_id not in trainer_id_list:
                trainer_id_list.append(new_id)
                id_found = True
        ID = new_id
        Name = data.get('Name')
        Email = data.get('Email')
        Phone = data.get('Phone')
        trainer_data = "INSERT INTO trainer(ID, Name, Email, Phone) VALUES(" + str(ID) + ", '" + Name + "', '" + Email + "', '" + Phone + "');"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(trainer_data)
        conn.commit()
        conn.close()
        id_dict = {"Message":"Trainer was successfully created"}
        return jsonify(id_dict)
    elif request.method == 'GET':
        if data.get('ID') != None:
            ID = data.get('ID')
            get_trainer_data = "SELECT * FROM trainer WHERE ID =" + str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_trainer_data)
                row = c.fetchone()
                conn.close()
                id_dict = {"Trainer":row}
                return jsonify(id_dict)
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
        else:
            logger.error("An error ocurred")
            return "Error: Invalid ID", 500
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            trainer_id_list.remove(ID)
            delete_trainer = "DELETE FROM trainer WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_trainer)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            id_dict = {"Message":"Trainer was successfully deleted"}
            return jsonify(id_dict)
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/team', methods=['GET', 'POST', 'DELETE'])
def team():
    data = request.get_json()
    if request.method == 'POST':
        for param in team_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        id_found = False
        while id_found == False:
            new_id = rnd.randint(1, 999)
            if new_id not in team_id_list:
                team_id_list.append(new_id)
                id_found = True
        ID = new_id
        Name = data.get('Name')
        Manager = data.get('Manager')
        Wins = 0
        Losses = 0
        team_data = "INSERT INTO team(ID, Name, Manager, Wins, Losses) VALUES(" + str(ID) + ", '" + Name + "', " + str(Manager) + ", " + str(Wins) + ", " + str(Losses) + ");"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("pragma foreign_keys=ON")
        c.execute(team_data)
        conn.commit()
        conn.close()
        id_dict = {"Message":"Team was successfully created"}
        return jsonify(id_dict)
    elif request.method == 'GET':
        if data.get('ID') != None:
            ID = data.get('ID')
            get_team_data = "SELECT * FROM team WHERE ID =" + str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_team_data)
                row = c.fetchone()
                conn.close()
                id_dict = {"Team":row}
                return jsonify(id_dict)
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
        else:
            logger.error("An error ocurred")
            return "Error: Invalid ID", 500
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            team_id_list.remove(ID)
            delete_team = "DELETE FROM team WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_team)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            id_dict = {"Message":"Team was successfully deleted"}
            return jsonify(id_dict)
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/membership', methods=['POST', 'DELETE'])
def membership():
    data = request.get_json()
    if request.method == 'POST':
        for param in membership_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        PokeID = data.get('PokemonID')
        TeamID = data.get('TeamID')
        team_count_list.append(TeamID)
        if(team_count_list.count(TeamID) > 6):
            team_count_list.pop()
            logger.error("Too many pokemon in one team")
            return "Too many pokemon", 500
        else:
            membership_data = "INSERT INTO Membership(PokemonID, TeamID) VALUES(" + str(PokeID) + ", " + str(TeamID) + ");"
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("pragma foreign_keys=ON")
            c.execute(membership_data)
            conn.commit()
            conn.close()
            id_dict = {"Message":"Membership was successfully created"}
            return jsonify(id_dict)
    if request.method == 'DELETE':
        for param in membership_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        PokeID = data.get('PokemonID')
        TeamID = data.get('TeamID')
        team_count_list.remove(TeamID)
        delete_membership = "DELETE FROM membership WHERE TeamID = "+ str(TeamID) + " AND PokemonID = " + str(PokeID) + ";"
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            res = c.execute(delete_membership)
            conn.commit()
            conn.close()
        except Exception:
            logger.error("An error ocurred")
            return "Error: Invalid ID", 500
        id_dict = {"Message":"Membership was successfully deleted"}
        return jsonify(id_dict)
@app.route('/ranking', methods=['GET'])
def ranking():
    top_3 = []
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * from team;")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        team_info = list(row)
        record = row[3]/(row[4] + 1)
        team_info.append(record)
        teams_data.append(team_info)
    teams_data.sort(reverse=True, key=lambda x: x[5])
    for item in teams_data:
        top_3.append(item[1])
    top_3 = top_3[:3]
    id_dict = {"Top three teams": top_3}
    return jsonify(id_dict)
@app.route('/battle', methods=['POST'])
def course():
    data = request.get_json()
    if request.method == 'POST':
        for param in battle_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        team1 = data.get('team1')
        team2 = data.get('team2')
        if (team1 == team2):
            logger.error("Team cannot battle itself")
            return "Team cannot battle itself", 500
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT * from team WHERE ID ="+ str(team1) + ";")
        team1_data = c.fetchone()
        conn.commit()
        conn.close()
        team1_name = team1_data[1]
        team1_wins = team1_data[3]
        team1_losses = team1_data[4]
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT * from team WHERE ID ="+ str(team2) + ";")
        team2_data = c.fetchone()
        conn.commit()
        conn.close()
        team2_name = team2_data[1]
        team2_wins = team2_data[3]
        team2_losses = team2_data[4]
        team1_strength = 0
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT PokemonID from membership WHERE TeamID ="+ str(team1) + ";")
        rows1 = c.fetchall()
        conn.commit()
        conn.close()
        for row in rows1:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT Experience from pokemon WHERE ID ="+ str(row[0]) + ";")
            strength = c.fetchone()
            team1_strength += strength[0]
        team2_strength = 0
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT PokemonID from membership WHERE TeamID ="+ str(team2) + ";")
        rows2 = c.fetchall()
        conn.commit()
        conn.close()
        for row in rows2:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("SELECT Experience from pokemon WHERE ID ="+ str(row[0]) + ";")
            strength = c.fetchone()
            team2_strength += strength[0]
        if(team1_strength > team2_strength):
            team1_wins += 1
            team2_losses += 1
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("UPDATE team SET Wins =" + str(team1_wins) + " WHERE ID ="+ str(team1) + ";")
            c.execute("UPDATE team SET Losses =" + str(team2_losses) + " WHERE ID ="+ str(team2) + ";")
            conn.commit()
            conn.close()
            return team1_name + " wins"
        elif(team1_strength < team2_strength):
            team2_wins += 1
            team1_losses += 1
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("UPDATE team SET Wins =" + str(team2_wins) + "  WHERE ID ="+ str(team2) + ";")
            c.execute("UPDATE team SET Losses =" + str(team1_losses) + " WHERE ID ="+ str(team1) + ";")
            conn.commit()
            conn.close()
            return team2_name + " wins"
        else:
            return "Both teams have drawed"
        
app.run(host='127.0.0.1', port=9999)


