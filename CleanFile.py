# clean the csv dataset in file named spotify_millsongdata.csv

import pandas as pd

# read the csv file
data = pd.read_csv('spotify_millsongdata.csv')

# drop the columns that are not needed
data = data[['artist','song']]

# drop the rows that have missing values
data = data.dropna()


# combine the artist and song columns into one text file
data['text'] = data['song'] + ' by ' + data['artist'] + ' official'

# save the text column to a songs.txt file
data['text'].to_csv('songs.txt', index=False, header=False)
