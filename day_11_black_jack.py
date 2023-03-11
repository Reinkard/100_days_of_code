from random import choice

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'ace']

def game(player_hand, computer_hand, number_of_cards):
    """Add a specified number of cards to the player and computer hands."""
    for _ in range(number_of_cards):
        player_hand = add_card(player_hand)
        if sum(computer_hand) < 17:
            computer_hand = add_card(computer_hand)
    return player_hand, computer_hand


def add_card(hand):
    """Add a card to the hand, taking into account the value of aces."""
    next_card = choice(cards)
    if next_card == 'ace':
        if sum(hand) < 11:
            hand.append(11)
        else:
            hand.append(1)
    else:
        hand.append(next_card)
    return hand

def check_game(player, computer):
    """Check the result of the game and print the outcome."""
    win = f'You win! You have {sum(player)}, computer have {sum(computer)}'
    lose = f'You lose! You have {sum(player)}, computer have {sum(computer)}'
    draw = f'It`s a draw! You have {sum(player)}, computer have {sum(computer)}'
    if sum(player) > 21:
        print(lose)
    elif sum(computer) > 21:
        print(win)
    elif sum(player) == 21:
        print(win)
    elif sum(computer) == 21:
        print(lose)
    elif sum(player) and sum(computer) <= 21:
        if sum(player) > sum(computer):
            print(win)
        elif sum(player) < sum(computer):
            print(lose)
        else:
            print(draw)

black_jack = True
while black_jack:
    player_hand = []
    computer_hand = []

    start_game = input('Do you want to play a game of BlackJack?: Type "y" or "n": ')
    while start_game not in ['y', 'n']:
        start_game = input('Do you want to play a game of BlackJack?: Type "y" or "n": ')

    if start_game == 'y':
        player_hand, computer_hand = game(player_hand, computer_hand, 2)
        continue_game = True
        while continue_game:
            if sum(player_hand) >= 21:
                check_game(player_hand, computer_hand)
                continue_game = False
            else:
                user_choice = input(f"Your cards: {player_hand}, current score: {sum(player_hand)}\n"
                   f"Computers cards: {computer_hand[:-1]}\n"
                   f"Type 'y' to get another card or 'n' to pass: ")
                while user_choice not in ['y', 'n']:
                    user_choice = input("Please type 'y' or 'n': ")
                if user_choice == 'y':
                    player_hand, computer_hand = game(player_hand, computer_hand, 1)
                else:
                    check_game(player_hand, computer_hand)
                    continue_game = False

    elif start_game == 'n':
        black_jack = False
print('Goodbye!')
