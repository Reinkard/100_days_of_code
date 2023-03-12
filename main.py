from random import randrange, choice, shuffle
from os import system


def day1_project():
    from archive.day_01_band_name_generator import band_name
    input("Press Enter to continue...\n")

def day2_project():
    from archive.day_02_tip_calculator import tip_calculator
    input("Press Enter to continue...\n")

def day3_project():
    from archive.day_03_treasury_island import treasury_island
    input("Press Enter to continue...\n")


def day4_project():
    from archive.day_04_rock_paper_scissors import rock_paper_scissors
    input("Press Enter to continue...\n")


def day5_project():
    from archive.day_05_password_generator import password_generator
    input("Press Enter to continue...\n")


def day7_project():
    from archive.day_07_hangman import hangman
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
