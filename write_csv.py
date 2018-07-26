import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Soccer
matchs2 = db['Match2']
 
with open('matchs.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    odds_keys = ['home_team_goal', 'away_team_goal', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'IWH', 'IWD', 'IWA', 'LBH', 'LBD', 'LBA',
     'PSH', 'PSD', 'PSA', 'WHH', 'WHD', 'WHA', 'SJH', 'SJD', 'SJA', 'VCH', 'VCD', 'VCA', 'GBH', 'GBD', 
     'GBA', 'BSH', 'BSD', 'BSA']

    match = matchs2.find_one()
    keys = []
    for key, value in match.items():
        if key in odds_keys:
            keys.append(str(key))
    filewriter.writerow(keys)

    for match in matchs2.find():
        values = []
        for key, value in match.items():
            if key in odds_keys:
                values.append(str(value))
        filewriter.writerow(values)