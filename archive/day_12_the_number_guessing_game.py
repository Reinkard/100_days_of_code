from random import randint


def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty in ['easy', 'hard']:
            break
    if difficulty == 'hard':
        lives = 5
    elif difficulty == 'easy':
        lives = 10
    return lives


def check_number(guess_num, lives):
    while True:
        print(f"You have {lives} attempts to guess the number.")
        player_num = int(input("Make a guess: ")) # make a guess a number
        if guess_num < player_num:
            print("Too high!")
        elif guess_num > player_num:
            print("Too low!")
        elif guess_num == player_num:
            print(f"You won! It is {player_num}!")
            break
        if lives > 1: # if lives > 1 - player lose the one life
                lives -= 1
        else:
            print("You lose!") # if lives = 0 - game over
            break


def make_number():
    return randint(1, 100)


def game():
    print("Welcome to the Number Guessing Game!\n"
        "I`m thinking of a number between 1 and 100")
    lives = choose_difficulty()         # choose difficulty
    guess_number = make_number()        # create the random int number
    check_number(guess_number, lives)
    while True:
        user_choice = input("Do you want to play again? Type 'y' or 'n': ")
        if user_choice in ['y', 'n']:
            break
    if user_choice == 'n':
        print("Goodbye!")
        input("Press Enter...")
        exit()
    else:
        game()


game()
    