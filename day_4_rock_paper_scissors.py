from random import randrange

text_play_again = 'Do you want to play again? Type y or n: '

win = 0
lose = 0
draw = 0

play = True
while play:
    # player choise - 0, 1 or 2
    player_choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
    while player_choose != 0 and player_choose != 1 and player_choose != 2:
        player_choose = int(input('Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
    # computer choose
    computer_choose = randrange(0, 3)
    # draw
    if player_choose == computer_choose:
        print(f'Computer choose {computer_choose}')
        draw += 1
        play_again = input(f'Win: {win}, Lose: {lose}, Draw: {draw}, {text_play_again}')
    # win
    elif player_choose == computer_choose + 1 or computer_choose - player_choose == 2:
        print(f'Computer choose {computer_choose}')
        win += 1
        play_again = input(f'Win: {win}, Lose: {lose}, Draw: {draw}, {text_play_again}')
    # lose
    elif computer_choose == player_choose + 1 or player_choose - computer_choose == 2:
        print(f'Computer choose {computer_choose}')
        lose += 1
        play_again = input(f'Win: {win}, Lose: {lose}, Draw: {draw}, {text_play_again}')
    # if play again is No
    if play_again == 'n':
        play = False

print('Goodbye!')
