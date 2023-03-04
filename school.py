# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/school.sqlite')
datab = conn.cursor()

def students_from_city(db, city):
    """return a list of students from a specific city"""
    query ="""SELECT first_name
    From students
    WHERE  UPPER(birth_city) = upper(?)
    """
    db.execute(query,(city,))
    results =  db.fetchall()
    return results
