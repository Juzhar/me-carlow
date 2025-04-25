# -*- coding: utf-8 -*-
"""
HW10
"""
# API

from flask import Flask, request, jsonify
import sqlite3
import logging

logging.config.fileConfig('config.ini')

app = Flask(__name__)
logger = logging.getLogger(__name__)

db_path = "Data/school.db"
student_params = ['ID', 'Name', 'Email', 'Phone', 'Year', 'Status']
teacher_params = ['ID', 'Name', 'Email', 'Phone']
class_params = ['ID', 'Name', 'Department', 'TeacherID']
school_params = ['ID', 'Name']
department_params = ['ID', 'Name', 'School_ID']
course_params = ['ID', 'Name', 'Dept_ID']
@app.route('/student', methods=['POST', 'GET', 'DELETE'])
def student():
    data = request.get_json()
    if request.method == 'POST':
        for param in student_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        Email = data.get('Email')
        Phone = data.get('Phone')
        Year = data.get('Year')
        Status = data.get('Status')
        student_data = "INSERT INTO STUDENT(ID, Name, Email, Phone, Year, Status) VALUES(" + str(ID) + ", '" + Name + "', '" + Email + "', '" + Phone + "', '" + Year + "', '" + Status + "');"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(student_data)
        conn.commit()
        conn.close()
        id_dict = {"New Student ID":ID}
        return jsonify(id_dict)
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            delete_student = "DELETE FROM STUDENT WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_student)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return "Student deleted successfully"
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/student/<ID>', methods=['GET'])
def students_get(ID):
    if request.method == 'GET':
        get_student_data = "SELECT * FROM STUDENT WHERE ID =" + ID
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(get_student_data)
            row = c.fetchone()
            conn.close()
            return jsonify(row)
        except Exception:
            logger.error("An error ocurred")
            return "Error: Invalid ID", 500
@app.route('/student/phone', methods=['POST'])
def student_phone():
    if request.method == 'POST':
        if request.method == 'POST':
            if 'ID' in request.args and 'Phone' in request.args:
                ID = request.args.get('ID')
                Phone = request.args.get('Phone')
                update_student_phone = "UPDATE STUDENT SET Phone ="+ Phone +" WHERE ID =" + ID
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(update_student_phone)
                conn.commit()
                conn.close()
                return "Phone updated successfully"
            else:
                logger.error("An error ocurred")
                return "Error: Missing query parameters", 500
@app.route('/teacher', methods=['POST', 'GET', 'DELETE'])
def teacher():
    data = request.get_json()
    if request.method == 'POST':
        for param in teacher_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        Email = data.get('Email')
        Phone = data.get('Phone')
        teacher_data = "INSERT INTO TEACHER(ID, Name, Email, Phone) VALUES(" + str(ID) + ", '" + Name + "', '" + Email + "', '" + Phone + "');"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(teacher_data)
        conn.commit()
        conn.close()
        id_dict = {"New Teacher ID":ID}
        return jsonify(id_dict)
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            delete_teacher = "DELETE FROM TEACHER WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_teacher)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return "Teacher deleted successfully"
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/teacher/<ID>', methods=['GET'])
def teachers_get(ID):
    if request.method == 'GET':
        get_teacher_data = "SELECT * FROM TEACHER WHERE ID =" + ID
        if 'count' in request.args and request.args.get('count') == "true":
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_teacher_data)
                row = c.fetchone()
                teacher_ID = row[0]
                get_class_count = "SELECT COUNT(*) FROM CLASS WHERE TeacherID = " + str(teacher_ID)
                c.execute(get_class_count)
                class_count = c.fetchone()
                class_output = '{count: ' + str(class_count[0]) + '}'
                row_list = list(row)
                row_list.append(class_output)
                conn.commit()
                conn.close()
                return row_list
            except FileNotFoundError:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
        else:
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_teacher_data)
                row = c.fetchone()
                conn.close()
                return jsonify(row)
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
@app.route('/teacher/phone', methods=['POST'])
def teacher_phone():
    if request.method == 'POST':
        if 'ID' in request.args and 'Phone' in request.args:
            ID = request.args.get('ID')
            Phone = request.args.get('Phone')
            update_teacher_phone = "UPDATE TEACHER SET Phone ="+ Phone +" WHERE ID =" + ID
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            res = c.execute(update_teacher_phone)
            conn.commit()
            conn.close()
            return "Phone updated successfully"
        else:
            logger.error("An error ocurred")
            return "Error: Missing query parameters", 500
@app.route('/class', methods=['POST', 'GET', 'DELETE'])
def classes():
    if request.method == 'POST':
        data = request.get_json()
        Department = ''
        for param in class_params:
            if data.get(param) == None:
                if param != 'Department':
                    logger.error("Error: " + param + " is required")
                    return "Error: " + param + " is required", 500
                else:
                    Department = 'Misc.'
            else:
                if param == 'Department':
                    Department = data.get('Department')
        ID = data.get('ID')
        Name = data.get('Name')
        TeacherID = data.get('TeacherID')
        class_data = "INSERT INTO CLASS(ID, Name, Department, TeacherID) VALUES(" + str(ID) + ", '" + Name + "', '" + Department + "', " + str(TeacherID) + ");"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(class_data)
        conn.commit()
        conn.close()
        id_dict = {"New Class ID":ID}
        return jsonify(id_dict)
    elif request.method == 'DELETE':
        if 'ID' in request.args:
            ID = request.args.get('ID')
            delete_class = "DELETE FROM CLASS WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_class)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return "Class deleted successfully"
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500  
    elif request.method == 'GET':
        if 'count' in request.args and request.args.get('count') == "true":
            get_class_number = "SELECT COUNT(*) FROM CLASS"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_class_number)
                class_count = c.fetchone()
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return '{count: ' + str(class_count[0]) + '}'
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/class/<ID>', methods=['GET'])
def classes_get(ID):
    get_class_data = "SELECT * FROM CLASS WHERE ID =" + ID
    if request.method == 'GET':
        if 'count' in request.args and request.args.get('count') == "true":
            get_class_number = "SELECT COUNT(*) FROM CLASS"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_class_number)
                class_count = c.fetchone()
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return '{count: ' + str(class_count[0]) + '}'
        else:
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(get_class_data)
                row = c.fetchone()
                conn.close()
                return jsonify(row)
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
@app.route('/school', methods=['POST', 'GET', 'DELETE'])
def school():
    data = request.get_json()
    if request.method == 'POST':
        for param in school_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        school_data = "INSERT INTO SCHOOL(ID, Name) VALUES(" + str(ID) + ", '" + Name + "');"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(school_data)
        conn.commit()
        conn.close()
        id_dict = {"New School ID":ID}
        return jsonify(id_dict)
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            delete_school = "DELETE FROM SCHOOL WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_school)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return "School deleted successfully"
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/school/<ID>', methods=['GET'])
def schools_get(ID):
    if request.method == 'GET':
        get_school_data = "SELECT * FROM SCHOOL WHERE ID =" + ID
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(get_school_data)
            row = c.fetchone()
            conn.close()
            return jsonify(row)
        except Exception as e:
            logger.error("An error occurred: {" + e + "}")
            return "Error: Invalid ID", 500
@app.route('/department', methods=['POST', 'GET', 'DELETE'])
def department():
    data = request.get_json()
    if request.method == 'POST':
        for param in department_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        School_ID = data.get('School_ID')
        department_data = "INSERT INTO DEPARTMENT(ID, Name, School_ID) VALUES(" + str(ID) + ", '" + Name + "', " + str(School_ID) + ");"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        try:
            c.execute("pragma foreign_keys=ON")
            c.execute(department_data)
            conn.commit()
        except Exception as e:
            logger.error("An error occurred: {" + e + "}")
            return f"An error occurred: {e}", 500
        finally:    
            conn.close()
        id_dict = {"New Department ID":ID}
        return jsonify(id_dict)
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            delete_department = "DELETE FROM DEPARTMENT WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_department)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return "Department deleted successfully"
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/department/<ID>', methods=['GET'])
def departments_get(ID):
    if request.method == 'GET':
        get_department_data = "SELECT * FROM DEPARTMENT WHERE ID =" + ID
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(get_department_data)
            row = c.fetchone()
            conn.close()
            return jsonify(row)
        except Exception:
            logger.error("An error ocurred")
            return "Error: Invalid ID", 500
@app.route('/course', methods=['POST', 'GET', 'DELETE'])
def course():
    data = request.get_json()
    if request.method == 'POST':
        for param in course_params:
            if data.get(param) == None:
                logger.error("Error: " + param + " is required")
                return "Error: " + param + " is required", 500
        ID = data.get('ID')
        Name = data.get('Name')
        Dept_ID = data.get('Dept_ID')
        course_data = "INSERT INTO COURSE(ID, Name, Dept_ID) VALUES(" + str(ID) + ", '" + Name + "', " + str(Dept_ID) + ");"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        try:
            c.execute("pragma foreign_keys=ON")
            c.execute(course_data)
            conn.commit()
        except Exception as e:
            logger.error("An error occurred: {" + e + "}")
            return f"An error occurred: {e}", 500
        finally:    
            conn.close()
        id_dict = {"New Course ID":ID}
        return jsonify(id_dict)
    elif request.method == 'DELETE':
        if data.get('ID') != None:
            ID = data.get('ID')
            delete_course = "DELETE FROM COURSE WHERE ID = "+ str(ID) + ";"
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                res = c.execute(delete_course)
                conn.commit()
                conn.close()
            except Exception:
                logger.error("An error ocurred")
                return "Error: Invalid ID", 500
            return "Course deleted successfully"
        else:
            logger.error("An error ocurred")
            return "Error: ID is required", 500
@app.route('/course/<ID>', methods=['GET'])
def courses_get(ID):
    if request.method == 'GET':
        get_course_data = "SELECT * FROM COURSE WHERE ID =" + ID
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(get_course_data)
            row = c.fetchone()
            conn.close()
            return jsonify(row)
        except Exception:
            logger.error("An error ocurred")
            return "Error: Invalid ID", 500
app.run(host='127.0.0.1', port=1000)