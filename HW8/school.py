# -*- coding: utf-8 -*-
"""
HW8
"""
# API

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

student_params = ['ID', 'Name', 'Email', 'Phone', 'Year', 'Status']
teacher_params = ['ID', 'Name', 'Email', 'Phone']
class_params = ['ID', 'Name', 'Department', 'TeacherID']

@app.route('/student', methods=['POST', 'GET', 'DELETE'])
def student():
    data = request.get_json()
    try:
        students_df = pd.read_csv('Data/student.csv')
    except FileNotFoundError:
        students_df = pd.DataFrame(columns=student_params)
    if request.method == 'POST':
        for param in student_params:
            if data.get(param) == None:
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        Email = data.get('Email')
        Phone = data.get('Phone')
        Year = data.get('Year')
        Status = data.get('Status')
        new_row = [ID, Name, Email, Phone, Year, Status]
        students_df.loc[len(students_df)] = new_row
        students_df.to_csv('Data/student.csv', index=False)
        return "Student added successfully"
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            new_students_df = students_df[students_df['ID'] != ID]
            new_students_df.to_csv('Data/student.csv', index=False)
            return "Student deleted successfully"
        else:
            return "Error: ID is required", 500
@app.route('/student/<ID>', methods=['GET'])
def students_get(ID):
    try:
        students_df = pd.read_csv('Data/student.csv')
    except FileNotFoundError:
        return "Error: No data"
    if request.method == 'GET':
        for index, row in students_df.iterrows():
            if row['ID'] == int(ID):
                row_list = [row['ID'], row['Name'], row['Email'], row['Phone'], row['Year'], row['Status']]
                return jsonify(row_list) 
        return "Error: Invalid ID", 500
@app.route('/teacher', methods=['POST', 'GET', 'DELETE'])
def teacher():
    try:
        teachers_df = pd.read_csv('Data/teacher.csv')
    except FileNotFoundError:
        teachers_df = pd.DataFrame(columns=teacher_params)
    data = request.get_json()
    if request.method == 'POST':
        for param in teacher_params:
            if data.get(param) == None:
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        Email = data.get('Email')
        Phone = data.get('Phone')
        new_row = [ID, Name, Email, Phone]
        teachers_df.loc[len(teachers_df)] = new_row
        teachers_df.to_csv('Data/teacher.csv', index=False)
        return "Teacher added successfully"
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            new_teachers_df = teachers_df[teachers_df['ID'] != ID]
            new_teachers_df.to_csv('Data/teacher.csv', index=False)
            return "Teacher deleted successfully"
        else:
            return "Error: ID is required", 500
@app.route('/teacher/<ID>', methods=['GET'])
def teachers_get(ID):
    try:
        teachers_df = pd.read_csv('Data/teacher.csv')
    except FileNotFoundError:
        return "Error: No data"
    if request.method == 'GET':
        for index, row in teachers_df.iterrows():
            if row['ID'] == int(ID):
                if 'count' in request.args and request.args.get('count') == 'true':
                    try:
                        classes_df = pd.read_csv('Data/class.csv')
                    except FileNotFoundError:
                        return "Error: No data"
                    count = 0
                    for index, class_row in classes_df.iterrows():
                        if class_row['TeacherID'] == row['ID']:
                            count += 1
                    row_list = [row['ID'], row['Name'], row['Email'], row['Phone'], ("Count", count)]
                    return jsonify(row_list)
                else:
                    row_list = [row['ID'], row['Name'], row['Email'], row['Phone']]
                    return jsonify(row_list)
        return "Error: Invalid ID", 500
@app.route('/class', methods=['POST', 'GET', 'DELETE'])
def classes():
    try:
        classes_df = pd.read_csv('Data/class.csv')
    except FileNotFoundError:
        classes_df = pd.DataFrame(columns=class_params)
    if request.method == 'POST':
        data = request.get_json()
        Department = ''
        for param in class_params:
            if data.get(param) == None:
                if param != 'Department':
                    return "Error: " + param + " is required", 500
                else:
                    Department = 'Misc.'
            else:
                if param == 'Department':
                    Department = data.get('Department')
        ID = data.get('ID')
        Name = data.get('Name')
        TeacherID = data.get('TeacherID')
        new_row = [ID, Name, Department, TeacherID]
        classes_df.loc[len(classes_df)] = new_row
        classes_df.to_csv('Data/class.csv', index=False)
        return "Class added successfully"
    elif request.method == 'GET':
        if 'count' in request.args and request.args.get('count') == 'true':
            class_count = len(classes_df)
            return '{count: ' + str(class_count) + '}'
    elif request.method == 'DELETE':
        if 'ID' in request.args:
            ID = request.args.get('ID')
            new_classes_df = classes_df[classes_df['ID'] != int(ID)]
            new_classes_df.to_csv('Data/class.csv', index=False)
            return "Class deleted successfully"
        else:
            return "Error: ID is required", 500  
@app.route('/class/<ID>', methods=['GET'])
def classes_get(ID):
    try:
        classes_df = pd.read_csv('Data/class.csv')
    except FileNotFoundError:
        return "Error: No data"
    if request.method == 'GET':
        if 'count' in request.args and request.args.get('count') == 'true':
            class_count = len(classes_df)
            return '{count: ' + str(class_count) + '}'
        else:
            for index, row in classes_df.iterrows():
                if row['ID'] == int(ID):
                    row_list = [row['ID'], row['Name'], row['Department'], row['TeacherID']]
                    return jsonify(row_list)
            return "Error: Invalid ID", 500
app.run(host='127.0.0.1', port=1000)