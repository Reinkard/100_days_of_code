import random


def check(pg_letters, pg_symbols, pg_numbers):
    if pg_letters == 0:
        if pg_numbers == 0:
            return symbols
        elif pg_symbols == 0:
            return numbers
        else:
            return numbers + symbols
    elif pg_numbers == 0:
        if pg_symbols == 0:
            return letters
        else:
            return symbols + letters
    elif pg_symbols == 0:
        return letters + numbers
    else:
        return letters + symbols + numbers
    

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
pg_letters = int(input(f"How many letters would you like in your password?\n")) 
pg_symbols = int(input(f"How many symbols would you like?\n"))
pg_numbers = int(input(f"How many numbers would you like?\n"))
result = ''
while not (pg_letters == 0 and pg_numbers == 0 and pg_symbols == 0):
    pg_password_table = check(pg_letters, pg_symbols, pg_numbers)
    symbol = random.choice(pg_password_table)
    if symbol in letters:
        pg_letters -= 1
    elif symbol in symbols:
        pg_symbols -= 1
    elif symbol in numbers:
        pg_numbers -= 1
    else:
        continue
    result += symbol
print(result)