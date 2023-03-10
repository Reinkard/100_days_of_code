alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '.', '/', ',', '&', '?', ' ']


def caesar(direction, text, shift):
    if direction == 'decode':
        shift *= -1
    result = ''
    for symbol in text:
        result += alphabet[abs((alphabet.index(symbol) + shift) % 26)] if symbol in alphabet else symbol
    return result


clipher = True
while clipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ['encode', 'decode']:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print('Result is: ', caesar(direction, text, shift))
    play_again = input('Do you wat to decode/encode again?Type y(yes) or n(no): ')
    while play_again not in ['y', 'n']:
        play_again = input('Please type y(yes) or n(no): ')
    if play_again == 'n':
        clipher = False
print('Have a nice day, good bye!')