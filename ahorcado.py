import os
import random
import time

WRONG_LETTER_COUNT = 6

IMÁGENES_AHORCADO = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

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
  /|\  |
       |
       |
=========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========''']


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def get_random_word():
    with open('./archivos/datos.txt', 'r', encoding='utf-8') as f:
        list_word = list(map(lambda line: line.strip(), f))
    return normalize(random.choice(list_word)).upper()

def get_position_char(word_choice, letter):
    return [pos for pos, char in enumerate(word_choice) if char == letter]


def get_ahorcado(position):
    print(IMÁGENES_AHORCADO[position])


def run():
    wrong_letters = 0
    correct_letters = 0
    all_letters = ''

    word = get_random_word()
    
    count_letters = len(word)
    word_to_find = list(' _' * len(word))
    resultado = ''
    while resultado == '':
        try:
            os.system('cls')
            get_ahorcado(wrong_letters)

            word_to_find_str = ''.join(word_to_find)

            print(word_to_find_str)

            letter = input('Indique una letra: ')
            
            assert len(letter) == 1 and not letter.isnumeric(), 'Debe indicar una sola letra'
            
            letter = letter.upper()
            if all_letters.find(letter) < 0:
                
                all_letters += letter

                positions = get_position_char(word, letter)

                count_find_positions = len(positions)
                
                if count_find_positions > 0:
                    correct_letters += count_find_positions
                    for i in positions:
                        word_to_find[i+i+1] = letter.upper()
                else:
                    wrong_letters += 1

            if count_letters == correct_letters:
                resultado = 'CORRECTO!!'
                word_to_find_str = ''.join(word_to_find)
                print(word_to_find_str)
            if wrong_letters == WRONG_LETTER_COUNT:
                resultado = 'PERDISTES!! La palabra era ' + word
                get_ahorcado(wrong_letters)
        except AssertionError as ae:
            print(ae)
            time.sleep(2)
    
    print(resultado)



if __name__ == '__main__':
    run()