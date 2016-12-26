import sqlite3
import datetime

def init():
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS meals
    (id integer primary key, date text NOT NULL, time text NOT NULL, meal text NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS out
    (id integer primary key, date text NOT NULL, time text NOT NULL, type text)''')
    connection.commit()
    connection.close()

def add_meal(date, time, meal):
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    c.execute('''INSERT INTO meals(date,time,meal) VALUES (?,?,?)''', (date, time, meal))
    connection.commit()
    connection.close()


def go_out(date, time):
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    c.execute('''INSERT INTO out(date,time) VALUES (?,?)''', (date, time))
    connection.commit()
    connection.close()

def undo_meal():
    return "does things"

def undo_out():
    return "does things"
