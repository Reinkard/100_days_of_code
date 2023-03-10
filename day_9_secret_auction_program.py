from os import system


logo = '''

          _______  _        _______  _______  _______  _______   _________ _______    _______           _______ __________________ _______  _       
|\     /|(  ____ \( \      (  ____ \(  ___  )(       )(  ____ \  \__   __/(  ___  )  (  ___  )|\     /|(  ____ \\__   __/\__   __/(  ___  )( (    /|
| )   ( || (    \/| (      | (    \/| (   ) || () () || (    \/     ) (   | (   ) |  | (   ) || )   ( || (    \/   ) (      ) (   | (   ) ||  \  ( |
| | _ | || (__    | |      | |      | |   | || || || || (__         | |   | |   | |  | (___) || |   | || |         | |      | |   | |   | ||   \ | |
| |( )| ||  __)   | |      | |      | |   | || |(_)| ||  __)        | |   | |   | |  |  ___  || |   | || |         | |      | |   | |   | || (\ \) |
| || || || (      | |      | |      | |   | || |   | || (           | |   | |   | |  | (   ) || |   | || |         | |      | |   | |   | || | \   |
| () () || (____/\| (____/\| (____/\| (___) || )   ( || (____/\     | |   | (___) |  | )   ( || (___) || (____/\   | |   ___) (___| (___) || )  \  |
(_______)(_______/(_______/(_______/(_______)|/     \|(_______/     )_(   (_______)  |/     \|(_______)(_______/   )_(   \_______/(_______)|/    )_)
Welcome to the secret auction program!
                                                                                                                                                    
'''


auction = True
players = {}
while auction:
    print(logo)
    player = input('What is your name?: ')
    bid = int(input('What`s your bid?: $'))
    next_player = input('Are there any other biders? Type y or n: ')
    players[player] = bid
    while next_player not in ['y', 'n']:
        next_player = input('Are there any other biders? Please type y or n: ')
    if next_player == 'y':
        system('clear')
    elif next_player == 'n':
        auction = False
max_bid = max(players.values()) # find max value
for key, value in players.items():
    if max_bid == value:
        print(f'The winner is {key} with ${max_bid}')