from os import system

def secret_auction():
    auction = True
    players = {}
    while auction:
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


secret_auction()