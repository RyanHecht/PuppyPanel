import sqllite3
import datetime

def init():
    connection = sqllite3.connect('database.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS meals
    (id integer primary key, date text NOT NULL, time text NOT NULL, meal text NOT NULL)''')
    connection.commit()
    connection.close()

def add_meal(date, time, meal):
    return "does things"

def go_out(date, time):
    return "does things"

def undo_meal():
    return "does things"

def undo_out():
    return "does things"
