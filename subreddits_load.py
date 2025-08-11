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





for directory in directories:
    START = time.time()


    # Create an empty dataframe
    df = pd.DataFrame(columns=["author", "subreddit", "created_utc", "parent_id", "id", "body", "score"])


    # Iterate over the files in ascending order by filename, set number of files to process
    files = sorted([f for f in os.listdir(directory)])
    #files = files[:10]
    print(files)
