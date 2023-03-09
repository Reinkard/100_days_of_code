from random import choice

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
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
