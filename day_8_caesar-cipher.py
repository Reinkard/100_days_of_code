alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '.', '/', ',', '&', '?', ' ']


def encode(text, shift):
    result = ''
    for symbol in text:
        result += alphabet[abs((alphabet.index(symbol) + shift) % 26)] if symbol in alphabet else symbol
    return result


def decode(text, shift):
    result = ''
    for symbol in text:
        result += alphabet[abs((alphabet.index(symbol) - shift) % 26)] if symbol in alphabet else symbol
    return result

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    print('Result is: ', encode(text, shift))

if direction == 'decode':
    print('Result is: ', decode(text, shift))