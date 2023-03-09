alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '.', '/', ',', '&', '?', ' ']


def caesar(direction, text, shift):
    if direction == 'decode':
        shift *= -1
    result = ''
    for symbol in text:
        result += alphabet[abs((alphabet.index(symbol) + shift) % 26)] if symbol in alphabet else symbol
    return result


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print('Result is: ', caesar(direction, text, shift))
