import sys
from mysqlx import Row
import pymongo
import pandas as pd
import requests
import json
from datetime import datetime
import datetime

# URLs used:
    # TOKEN: https://developer.spotify.com/console/get-recently-played/
    # PROJECT INSPIRATION: https://github.com/karolina-sowinska/free-data-engineering-course-for-beginners/blob/master/main.py

# By typing in capital letters we'll create a constant, which, contrary to variables, these are inmutable
USER_DB = 'mongodb://localhost:27017' # not sure if it will work
USER_ID = '' # Spotify user id
USER_TOKEN = '' # Token generated

#--------------------------------------------------------------------------------------------------------

# Let's start the process

# Creating a validation function
def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Check if dataframe is empty
    if df.empty:
        print('No songs downloaded. Finished')
        return False
    
    # Primary key checking
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception('Primary key violated')

    # Checking nulls
    if df.isnull().values.any():
        raise Exception('Null values found')
    
    # Check timestamps
    last = datetime.datetime.now() - datetime.timedelta(days = 1)
    last = last.replace(hour = 0, minute = 0, second = 0, microsecond = 0)

    timestamps = df['timestamp'].tolist()
    for timestamp in timestamps:
        if datetime.datetime.strptime(timestamp, '%Y-%m-%d') != last:
            raise Exception('At least one song does not have a timestamp')
    
    return True

#--------------------------------------------------------------------------------------------------------
# ETL Process

# EXTRACT (E)
if __name__ == '__main__':
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token}'.format(token = USER_TOKEN)
    }

    # We'll convert timestamps on the API to Unix timestamps
    curr = datetime.datetime.now()
    last = curr - datetime.timedelta(days = 1)
    unix_timestamp = int(last.timestamp()) * 1000

    # Requesting data from url
    req = requests.get('https://api.spotify.com/v1/me/player/recently-played?after={time}'.format(time = unix_timestamp), headers = headers)

    # Read data as json format
    try:
        if(req.status_code == 200):
            #data = req.json()
            data_raw = json.loads(req.text)
    except Exception as e:
        print('Operation could not be completed' + str(e))
    
    # Also works:
    #data = req.json()
    #print(data.keys())

    # Creation of empty dictionaries
    song_names = []
    artists_names = []
    played_at_list = []
    timestamps = []

    # Extracting the relevant data for the lists (can be seen by using print or .keys())
    for song in data_raw['items']:
        song_names.append(song['track']['name'])
        artists_names.append(song['track']['album']['artists'][0]['name'])
        played_at_list.append(song['played_at'])
        timestamps.append(song['played_at'][0:10])
    
    # Prepare data for Pandas df conversion
    song_dict = {
        'song_name': song_names,
        'artist_name': artists_names,
        'played_at': played_at_list,
        'timestamp': timestamps
    }

    #--------------------------------------------------------------------------------------------------------
    # JSON file

    try:
        jsonString = json.dumps(song_dict, separators = (',', ':'))
        jsonFile = open('spotify_etl.json', 'w')
        jsonFile.write(jsonString)
        jsonFile.close()
        print('JSON File succesfully generated!')
    except:
        print('Error')
        # works, order is important

    # Pandas dataframe creation
    df = pd.DataFrame(song_dict, columns = ['song_name', 'artist_name', 'played_at', 'timestamp'])

# TRANSFORM (T)
if check_if_valid_data(df):
    print('Data validation correct. Proceed to LOAD phase.')

# LOAD (L)
# I will be loading the data into MongoDB local db using PyMongo

try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
except Exception as e:
    print('Connection could not be done' + str(e))
    sys.exit()

db = client['spotify_etl_db']
collection = db['spotify_data']

db_dict = song_dict
db_dict = [db_dict]
# Dictionaries will cause problems here, maybe trying bulk ops

'''try:
    bulk = collection.insert_many(song_dict)
except:
    print('Next step.')
'''

mongo_insert = collection.insert_many(db_dict)

print('ETL-Pipeline process completed!')