# -*- coding: utf-8 -*-
"""
HW9
"""
# Initial

import sqlite3
db_path = "Data/school.db"
student_table = "CREATE TABLE IF NOT EXISTS STUDENT ( ID integer, Name text, Email text, Phone text, Year text, Status text);"
teacher_table = "CREATE TABLE IF NOT EXISTS TEACHER ( ID integer, Name text, Email text, Phone text);"
class_table = "CREATE TABLE IF NOT EXISTS CLASS ( ID integer, Name text, Department text, TeacherID integer);"
schools_table = "CREATE TABLE IF NOT EXISTS SCHOOLS ( ID integer, Name text, City text);"
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(student_table)
    c.execute(teacher_table)
    c.execute(class_table)
    c.execute(schools_table)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print("unable to connect to database", e)
