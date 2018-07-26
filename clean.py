from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Soccer
matchs = db['Match']
matchs2 = db['Match2']
for match in matchs.find():
    odds_keys = ['B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'IWH', 'IWD', 'IWA', 'LBH', 'LBD', 'LBA',
     'PSH', 'PSD', 'PSA', 'WHH', 'WHD', 'WHA', 'SJH', 'SJD', 'SJA', 'VCH', 'VCD', 'VCA', 'GBH', 'GBD', 
     'GBA', 'BSH', 'BSD', 'BSA']
    for key, value in match.items():
        if key in odds_keys and type(value) == str:
            match[key] = float(value)
        elif key in odds_keys and value is None:
            if key[-1] is 'H': 
                match[key] = match['B365H']
            elif key[-1] is 'D': 
                match[key] = match['B365D']
            elif key[-1] is 'A': 
                match[key] = match['B365A']
    
    new_match = {
        "home_team_goal": match['home_team_goal'],
        "away_team_goal": match['away_team_goal'],
        "B365H" : match['B365H'], 
        "B365D" : match['B365D'], 
        "B365A" : match['B365A'], 
        "BWH" : match['BWH'], 
        "BWD" : match['BWD'], 
        "BWA" : match['BWA'], 
        "IWH" : match['IWH'], 
        "IWD" : match['IWD'], 
        "IWA" : match['IWA'], 
        "LBH" : match['LBH'], 
        "LBD" : match['LBD'], 
        "LBA" : match['LBA'], 
        "PSH" : match['PSH'], 
        "PSD" : match['PSD'], 
        "PSA" : match['PSA'], 
        "WHH" : match['WHH'], 
        "WHD" : match['WHD'], 
        "WHA" : match['WHA'], 
        "SJH" : match['SJH'], 
        "SJD" : match['SJD'], 
        "SJA" : match['SJA'], 
        "VCH" : match['VCH'], 
        "VCD" : match['VCD'], 
        "VCA" : match['VCA'], 
        "GBH" : match['GBH'], 
        "GBD" : match['GBD'], 
        "GBA" : match['GBA'], 
        "BSH" : match['BSH'], 
        "BSD" : match['BSD'], 
        "BSA" : match['BSA']
    }
    matchs2.insert_one(new_match)