'''
Silly-man's multiprocessing :)

Run multiple instances of this script or make it better.
'''

import sqlite3
import pickle
import pandas as pd
import sqlite3
import colorama


# create table with unique id column and a text column, called walls1337bot

conn = sqlite3.connect('walls1337bot.db')
c = conn.cursor()
# create table if it doesnt exist:
c.execute('''CREATE TABLE IF NOT EXISTS walls1337bot
             (id TEXT PRIMARY KEY, train_text TEXT, score INT, length INT)''')
conn.commit()
#conn.close()



files = ["2016_j_wallstreetbets.pkl", "2017_j_wallstreetbets.pkl", "2018_j_wallstreetbets.pkl"]


df = pd.DataFrame()


conn = sqlite3.connect('walls1337bot.db')
c = conn.cursor()



for file in files:
    with open(file, 'rb') as f:
        data = pickle.load(f)
        df = df.append(data)
        
# remove first 3 characters in all rows of the "parent_id" column
df['parent_id'] = df['parent_id'].str[3:]


