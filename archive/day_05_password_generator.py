import random


def password_generator():
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
            result.append(random.choice(letters))
        for sym in range(pg_symbols):
            result.append(random.choice(symbols))
        for num in range(pg_numbers):
            result.append(random.choice(numbers))
        random.shuffle(result)
        print(*result, sep='')
 