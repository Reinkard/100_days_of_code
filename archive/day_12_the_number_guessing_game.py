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


def make_number():
    return randint(1, 100)


def game():
    print("Welcome to the Number Guessing Game!\n"
        "I`m thinking of a number between 1 and 100")
    while True:
        lives = choose_difficulty()
        number = make_number()
        while True:
            print(f"You have {lives} attempts to guess the number.")
            guess_number = int(input("Make a guess: "))
            if guess_number < number:
                print("Too low!")
            elif guess_number > number:
                print("Too high!")
            elif guess_number == number:
                print(f"You won! It is {number}!")
                break
            if lives > 1:
                lives -= 1
            else:
                print("You lose!")
                break
        while True:
            user_choice = input("Do you want to play again? Type 'y' or 'n': ")
            if user_choice in ['y', 'n']:
                break
        if user_choice == 'n':
            print("Goodbye!")
            input("Press Enter...")
            break


game()
    