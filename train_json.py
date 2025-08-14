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


# save the train_text column of the database to json formatted like {"sample": "text"}

MIN_SCORE = 7
MIN_LEN = 5
MAX_CHARS = 7500
c.execute("SELECT train_text FROM walls1337bot WHERE score >= ? AND length >= ?", (MIN_SCORE, MIN_LEN))
rows = c.fetchall()
print('Number of samples with these settings:',len(rows))

# save each row of train_text to json file such that it looks like
# {"sample": "text"} per line



