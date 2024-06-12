import datetime

game1 = {
    'nama': 'CSGO',
    'publisher': 'Valve',
    'steam': True,
    'peak_player': 1_519_457,
    'tanggal_rilis': datetime.datetime(2012, 8, 21),
}

game2 = {
    'nama': 'Genshin Impact',
    'publisher': 'Hoyolab',
    'steam': False,
    'peak_player': 63_000_000,
    'tanggal_rilis': datetime.datetime(2020, 9, 28)
}

game3 = {
    'nama': 'Honkai Star Rail',
    'publisher': 'Hoyolab',
    'steam': False,
    'peak_player': 24_000_000,
    'tanggal_rilis': datetime.datetime(2023, 4, 26)
}

game4 = {
    'nama': 'Dota 2',
    'publisher': 'Valve',
    'steam': True,
    'peak_player': 1_295_114,
    'tanggal_rilis': datetime.datetime(2009, 7, 9)
}
game5 = {
    'nama': 'League of Legends',
    'publisher': 'Riot Games',
    'steam': False,
    'peak_player': 8_000_000,
    'tanggal_rilis': datetime.datetime(2009, 10, 27)
}

data_games = {
    'GAME001': game1,
    'GAME002': game2,
    'GAME003': game3,
    'GAME004': game4,
    'GAME005': game5,
}

print(f'{'key':<8} {'Nama':<18} {'Publisher':<11} {'Steam':<6} {'Peak Players':<13} {'Tanggal Rilis':<8}')
print(f'-'*74)

for i in data_games:
    key = i
    nama = data_games[key]['nama']
    publisher = data_games[key]['publisher']
    steam = data_games[key]['steam']
    peak_player = data_games[key]['peak_player']
    tanggal_rilis = data_games[key]['tanggal_rilis'].strftime('%x')
    
    print(f'{key:<8} {nama:<18} {publisher:<11} {steam:^6} {peak_player:<13,.0f} {tanggal_rilis:<8}')
    


























