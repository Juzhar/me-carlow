# -*- coding: utf-8 -*-
"""
HW11
"""
# Initial

import sqlite3
db_path = "Data/school.db"
student_table = "CREATE TABLE IF NOT EXISTS STUDENT ( ID integer PRIMARY KEY, Name text NOT NULL, Email text NOT NULL, Phone text NOT NULL, Year text NOT NULL, Status text NOT NULL);"
teacher_table = "CREATE TABLE IF NOT EXISTS TEACHER ( ID integer PRIMARY KEY, Name text NOT NULL, Email text NOT NULL, Phone text NOT NULL);"
class_table = "CREATE TABLE IF NOT EXISTS CLASS ( ID integer PRIMARY KEY, Name text NOT NULL, Department text NOT NULL, TeacherID integer NOT NULL);"
schools_table = "CREATE TABLE IF NOT EXISTS SCHOOL ( ID integer PRIMARY KEY, Name text NOT NULL);"
departments_table = "CREATE TABLE IF NOT EXISTS DEPARTMENT ( ID integer PRIMARY KEY, Name text NOT NULL, School_ID integer NOT NULL, FOREIGN KEY(School_ID) REFERENCES SCHOOL(ID)) STRICT;"
courses_table = "CREATE TABLE IF NOT EXISTS COURSE ( ID integer PRIMARY KEY, Name text NOT NULL, Dept_ID integer NOT NULL, FOREIGN KEY(Dept_ID) REFERENCES DEPARTMENT(ID)) STRICT;"

try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(student_table)
    c.execute(teacher_table)
    c.execute(class_table)
    c.execute(schools_table)
    c.execute(departments_table)
    c.execute(courses_table)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print("unable to connect to database", e)
