import os
import json
import pandas as pd
from tqdm import tqdm
import time
import pickle

# Set the directory

directories = ["2016_j", "2017_j", "2018_j"]

target_subreddits = ["wallstreetbets"]


'''target_subreddits = ["wallstreetbets",
                     "askreddit",
                     "showerthoughts",
                     "todayilearned",
                     "cleanjokes",
                     "murderedbywords",
                     "jokes",
                     "funny",
                     "roastme",
                     "dadjokes",
                     "madlads",
                     "cringe",
                     "wtf",
                     "memes",
                     "publicfreakout",
                     "insanepeoplefacebook",
                     "facepalm",
                     "holdmybeer",
                     "instant_regret",
                     "idiotsincars",
                     "nonononoyes",
                     "yesyesyesno",
                     "maliciouscompliance",]'''
