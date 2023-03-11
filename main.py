from random import randrange, choice, shuffle
from os import system

def day1_project():
    """ 
    day 1 project: band name generator
    """
    def band_name(city, pets_name):
        """
        Print your band name
        """
        print('Your band name is', city, pets_name)


    print('Welcome to the Band Name Generator.')
    city = input('What`s name of the city you grew up in? \n')
    pets_name = input('What`s you pets name? \n')
    band_name(city, pets_name)
    input("Press Enter to continue...\n")


def day2_project():
    """
    day 2 project: tip calculator
    """
    def pay(bill, percentage, people):
        """
        Percentage to give + bill on peoples persons
        """
        return '{:.2f}'.format((percentage / 100 * bill + bill) / people)


    print('Welcome to the tip calculator.')
    bill = float(input('What is the total bill? $'))
    percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? %'))
    while percentage != 10 and percentage != 12 and percentage != 15:
        percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? %'))
    people = int(input('How mant people to split the bill? '))
    print('Each person should pay:', pay(bill, percentage, people), '$')
    input("Press Enter to continue...\n")

def day3_project():
    """
    day 3 project: treasury island
    """
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`..*. . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
    def part_1(choose):
        if choose == 'left':
            choose_2 = input('Do you swim of wait? Type swim or wait: ')
            part_2(choose_2)
        else:
            print('Fall into a hole. Game Over')


    def part_2(choose):
        if choose == 'wait':
            choose_3 = input('Which door do you choose? Type red, blue or yellow: ')
            part_3(choose_3)
        else:
            print('Attacket by trout. Game Over')


    def part_3(choose):
        if choose == 'red':
            print('Burned by fire. Game Over.')
        elif choose == 'blue':
            print('Eaten by beasts. Game Over.')
        elif choose == 'yellow':
            print('''
8b        d8                                                                               88              
 Y8,    ,8P                                                                                ""              
  Y8,  ,8P                                                                                                 
   "8aa8" ,adPPYba,  88       88    ,adPPYYba, 8b,dPPYba,  ,adPPYba,    8b      db      d8 88 8b,dPPYba,   
    `88' a8"     "8a 88       88    ""     `Y8 88P'   "Y8 a8P_____88    `8b    d88b    d8' 88 88P'   `"8a  
     88  8b       d8 88       88    ,adPPPPP88 88         8PP"""""""     `8b  d8'`8b  d8'  88 88       88  
     88  "8a,   ,a8" "8a,   ,a88    88,    ,88 88         "8b,   ,aa      `8bd8'  `8bd8'   88 88       88  
     88   `"YbbdP"'   `"YbbdP'Y8    `"8bbdP"Y8 88          `"Ybbd8"'        YP      YP     88 88       88  
                                                                                                           
            ''')
        else:
            print('Game Over')

    while True:
        print('Welcome to Treasure Island. Your mission is to find the treasure.')
        choose_1 = input('You are at the cross road. Where do you want to go? Type left of right: ')
        part_1(choose_1)
        continue_choise = input("Do you want to play again? Type 'y' or 'n': ")
        while continue_choise not in ['y', 'n']:
            continue_choise = input("Do you want to play again? Type 'y' or 'n': ")
        if continue_choise == 'n':
            break
    input("Press Enter to continue...\n")


def day4_project():
    """
    day 4 project: rock paper scissors
    """
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

    print(f'The final score is: \nWin: {win}, Lose: {lose}, Draw: {draw}\n Goodbye!')
    input("Press Enter to continue...\n")


def day5_project():
    """
    day 5 project: password generator
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    pg_letters = int(input(f"How many letters would you like in your password?\n")) 
    pg_symbols = int(input(f"How many symbols would you like?\n"))
    pg_numbers = int(input(f"How many numbers would you like?\n"))
    pg_num_of_passwords = int(input("How many passwords would you like?\n"))
    for passwords in range(pg_num_of_passwords):
        result = []
        for let in range(pg_letters):
            result.append(choice(letters))
        for sym in range(pg_symbols):
            result.append(choice(symbols))
        for num in range(pg_numbers):
            result.append(choice(numbers))
        shuffle(result)
        print(*result, sep='')
    input("Press Enter to continue...\n")


def day7_project():
    """
    day 7 project: hangman
    """
    stages = ['''
    +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    ''', 
    '''
    +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''', 
    '''
    +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''', 
    '''
    +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', 
    '''
    +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''', 
    '''
    +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''', 
    '''
    +---+
     |   |
         |
         |
         |
         |
    =========
    ''']
    # словник загадуваних слів
    word_list = ['mouse', 'keyboard', 'monitor', 'laptop'] 

    word_choose = choice(word_list)  # вибір слова
    lives = 6  # кількість спроб
    game = True
    word = []  # пусте слово "_ _ _ _", довжина якого залежить від довжини загадуваного слова
    for _ in range(len(word_choose)):
        word.append('_')

    while game:
        print('Word is: ', *word, stages[lives])
        letter_choose = input(
            f'You have {lives} lives left! Guess a letter: ').lower()
        # йде перевірка - якщо загадувана буква є у слові - то символ "_" заміняється на цю букву
        for number_of_string in range(len(word_choose)):
            if letter_choose == word_choose[number_of_string]:
                word[number_of_string] = letter_choose
        # якщо букви у слові немає - віднімається одне життя. Якщо значення 0 - гра закінчується
        if letter_choose not in word_choose:
            lives -= 1
            if lives == 0:
                print('Game over!')
                game = False
        # якщо символів "_" більше не залишилось - гру закінчено, гравець виграв
        if '_' not in word:
            print('You win! The word is', word_choose)
            game = False
    input("Press Enter to continue...\n")


def day8_project():
    """
    day 8 project: caesar cipher
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def caesar(direction, text, shift):
        # decode/encode your text
        if direction == 'decode':
            shift *= -1
        result = ''
        for symbol in text:
            result += alphabet[abs((alphabet.index(symbol) + shift) % 26)] if symbol in alphabet else symbol
        return result


    clipher = True
    while clipher:
        # ask user decode/encode text
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        while direction not in ['encode', 'decode']:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print('Result is: ', caesar(direction, text, shift))
        # ask user to play again
        play_again = input('Do you want to decode/encode again?Type y(yes) or n(no): ')
        while play_again not in ['y', 'n']:
            play_again = input('Please type y(yes) or n(no): ')
        if play_again == 'n':
            clipher = False
    print('Have a nice day, good bye!')
    input("Press Enter to continue...\n")


def day9_project():
    """
    day 9 project: hangman
    """
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
    input("Press Enter to continue...\n")


def day10_project():
    """
    day 10 project: caesar cipher
    """
    logo = """
        _..._                          _..._     
        .-'_..._''.           .---.    .-'_..._''.  
    .' .'      '.\          |   |  .' .'      '.\ 
    / .'                     |   | / .'            
    . '                       |   |. '              
    | |                 __    |   || |              
    | |              .:--.'.  |   || |              
    . '             / |   \ | |   |. '              
    \ '.          .`" __ | | |   | \ '.          . 
    '. `._____.-'/ .'.''| | |   |  '. `._____.-'/ 
        `-.______ / / /   | |_'---'    `-.______ /  
                `  \ \._,\ '/                  `   
                    `--'  `"                       
    """


    def addition(num_1, num_2) -> float:
        """
        Додає два числа.
        Args:
            num_1 (float): Перше число.
            num_2 (float): Друге число.
        Returns:
            float: Сума num_1 та num_2.
        """
        return num_1 + num_2


    def substraction(num_1, num_2) -> float:
        """
        Віднімає два числа.
        Args:
            num_1 (float): Перше число.
            num_2 (float): Друге число.
        Returns:
            float: Різниця num_1 та num_2.
        """
        return num_1 - num_2


    def multiplication(num_1, num_2) -> float:
        """
        Множення між двома числами.
        Args:
            num_1 (float): Перше число.
            num_2 (float): Друге число.
        Returns:
            float: Добуток num_1 та num_2.
        """
        return num_1 * num_2


    def division(num_1, num_2) -> float:
        """
        Ділить два числа.
        Args:
            num_1 (float): Перше число.
            num_2 (float): Друге число.
        Returns:
            float: Частка num_1 та num_2.
        """
        return num_1 / num_2


    def modulus(num_1, num_2) -> float:
        """
        Виначає остачу між ділення двох чисел.
        Args:
            num_1 (float): Перше число.
            num_2 (float): Друге число.
        Returns:
            float: Остача між діленням num_1 та num_2.
        """
        return num_1 % num_2


    def exponentiation(num_1, num_2) -> float:
        """
        Зведення числа num_1 в степінь num_2.
        Args:
            num_1 (float): Перше число.
            num_2 (float): Друге число.
        Returns:
            float: num_1 в степені num_2.
        """
        return num_1 ** num_2


    operation = {'+': addition, '-': substraction, '*': multiplication,
                '/': division, '%': modulus, '**': exponentiation}

    print(logo)
    calculator = True
    while calculator:
        first_number = float(input('What`s the first number?: '))
        calculate_1st_number = True
        while calculate_1st_number:
            for keys in operation.keys():
                print(*keys, sep='')
            choise = input('Pick an operation: ')
            second_number = float(input('What`s the next number?: '))
            funct = operation[choise]
            first_number = funct(first_number, second_number)
            choise_with_result = input(
                f'Type "y" to continue with {first_number}, "n" to a new calculation or "e" to exit: ')
            while choise_with_result not in ['y', 'n', 'e']:
                choise_with_result = input(
                    f'Type "y" to continue with {first_number}, "n" to a new calculation or "e" to exit: ')
            if choise_with_result == 'n':
                calculate_1st_number = False
            elif choise_with_result == 'e':
                calculate_1st_number = False
                calculator = False
    print('Goodbye!')
    input("Press Enter to continue...\n")


def day11_project():
    """
    day 11 project: caesar cipher
    """
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
        elif sum(player) and sum(computer) <= 21:
            if sum(player) > sum(computer):
                print(win)
            elif sum(player) < sum(computer):
                print(lose)
            elif sum(player) == 21:
                print(win)
            elif sum(computer) == 21:
                print(lose)
            elif sum(player) == sum(computer):
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
    input("Press Enter to continue...\n")


project_functions = {
    "1": day1_project,
    "2": day2_project,
    "3": day3_project,
    "4": day4_project,
    "5": day5_project,
    "7": day7_project,
    "8": day8_project,
    "9": day9_project,
    "10": day10_project,
    "11": day11_project
}

while True:
    project_choice = input("Enter project number:\n"
                        "1. band name generator\n"
                        "2. tip calculator\n"
                        "3. treasury island\n"
                        "4. rock paper scissors\n"
                        "5. password generator\n"
                        "7. hangman\n"
                        "8. caesar cipher\n"
                        "9. secret auction\n"
                        "10. calc\n"
                        "11. black jack\n"
                        "or q to quit\n"
                        "enter: "
                        )
    if project_choice == "q":
        break
    selected_function = project_functions.get(project_choice)
    if selected_function:
        selected_function()
    else:
        print("Invalid choice")
