from random import randrange

def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    win = 0
    lose = 0
    draw = 0

    text_play_again = 'Do you want to play again? Type y or n: '

    choose_picture = [rock, paper, scissors]

    play = True
    while play:
        # player choise - 0, 1 or 2
        player_choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
        while player_choose not in range(0, 3):
            player_choose = int(input('Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
        # computer choose
        computer_choose = randrange(0, 3)
        # draw
        if player_choose == computer_choose:
            print(f'Computer choose: \n {choose_picture[computer_choose]}')
            print(f'You choose: \n {choose_picture[player_choose]}')
            print('It`s a draw!')
            draw += 1
            play_again = input(f'Score: \nWin: {win}, Lose: {lose}, Draw: {draw} \n{text_play_again}')
        # win
        elif player_choose == computer_choose + 1 or computer_choose - player_choose == 2:
            print(f'Computer choose: \n {choose_picture[computer_choose]}')
            print(f'You choose: \n {choose_picture[player_choose]}')
            print('You won!')
            win += 1
            play_again = input(f'Score: \nWin: {win}, Lose: {lose}, Draw: {draw} \n{text_play_again}')
        # lose
        elif computer_choose == player_choose + 1 or player_choose - computer_choose == 2:
            print(f'Computer choose: \n {choose_picture[computer_choose]}')
            print(f'You choose: \n {choose_picture[player_choose]}')
            print('You lose!')
            lose += 1
            play_again = input(f'Score: \nWin: {win}, Lose: {lose}, Draw: {draw} \n{text_play_again}')
        # if play again is No
        if play_again == 'n':
            play = False

    print(f'The final score is: \nWin: {win}, Lose: {lose}, Draw: {draw}\nGoodbye!')

rock_paper_scissors()
