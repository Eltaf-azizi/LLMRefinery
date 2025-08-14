import sqlite3
import pandas as pd
import sqlite3
import json


# create table with unique id column and a text column, called walls1337bot


conn = sqlite3.connect('walls1337bot.db')
c = conn.cursor()

# create table if it doesnt exist:
c.execute('''CREATE TABLE IF NOT EXISTS walls1337bot
             (id TEXT PRIMARY KEY, train_text TEXT, score INT, length INT)''')
conn.commit()

