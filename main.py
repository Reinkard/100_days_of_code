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
    from archive.day_08_caesar_cipher import caesar_cipher
    input("Press Enter to continue...\n")


def day9_project():
    from archive.day_09_secret_auction_program import secret_auction
    input("Press Enter to continue...\n")


def day10_project():
    from archive.day_10_calc import calc
    input("Press Enter to continue...\n")


def day11_project():
    from archive.day_11_black_jack import black_jack_game
    input("Press Enter to continue...\n")


def day12_project():
    from archive.day_12_the_number_guessing_game import game
    input("Press Enter to continue...\n")


def day14_project():
    from archive.day_14_higher_lower_game import higher_lower
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
    "11": day11_project,
    "12": day12_project,
    "14": day14_project,
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
                        "12. the number guessing game\n"
                        "14. higher lower game\n"
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
