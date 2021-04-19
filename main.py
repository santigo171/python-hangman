import os
import sys
import random
from random import randint
import time
import ast

TERMINAL_SIZE = os.get_terminal_size()
columns = TERMINAL_SIZE.columns
rows = TERMINAL_SIZE.lines
# ------------- Sprites:
HANGMAN_TITLE = """██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                    by David Hurtado"""

SMALL_TITLE = """\n█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█\n
"""

HANGMAN_PICS = ['''  +---+
  |   |
      |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

alphabet = {
    'a': '▄▀█\n█▀█',
    'b': '█▄▄\n█▄█',
    'c': '█▀▀\n█▄▄',
    'd': '█▀▄\n█▄▀',
    'e': '█▀▀\n██▄',
    'f': '█▀▀\n█▀░',
    'g': '█▀▀\n█▄█',
    'h': '█░█\n█▀█',
    'i': '░█░\n░█░',
    'j': '░░█\n█▄█',
    'k': '█▄▀\n█░█', 
    'l': '█░░\n█▄▄',
    'm': '█▀▄▀█\n█░▀░█',
    'n': '█▄░█\n█░▀█',
    'o': '█▀█\n█▄█',
    'p': '█▀█\n█▀▀',
    'q': '█▀█\n▀▀█',
    'r': '█▀█\n█▀▄',
    's': '█▀\n▄█',
    't': '▀█▀\n░█░',
    'u': '█░█\n█▄█',
    'v': '█░█\n▀▄▀',
    'w': '█░█░█\n▀▄▀▄▀',
    'x': '▀▄▀\n█░█',
    'y': '█▄█\n░█░',
    'z': '▀█░\n█▄░'
}

# ------------- Colors:
def color(color, string):
    color_list = ['purple', 'cyan', 'blue', 'green', 'yellow', 'red']
    if color == '':
        color = random.choice(color_list)
    if color == 'purple':
        style = "\033[95m"
    elif color == 'cyan':
        style = "\033[96m"
    elif color == 'blue':
        style = "\033[94m"
    elif color == 'green':
        style = '\033[92m'
    elif color == 'yellow':
        style = '\033[93m'
    elif color == 'red':
        style = '\033[91m'
    elif color == 'bold':
        style = '\033[1m'
    elif color == 'underline':
        style = '\033[4m'
    return style + string + '\033[0m'


# ------------- Messages:
help_message = f"""{color('bold', "HANGMAN Game, created by David Hurtado")} {color('blue', "@santigo171.")}

{color('bold', "hangman -h")}: Show the help message.
{color('bold', "hangman -c")}: Will make some config changes.

{color('bold', "hangman -p")}: Play an Hangman Game.

{color('bold', "hangman -l")}: Show the word list.
{color('bold', "hangman -a word")}: Add an word to the word list.
{color('bold', "hangman -d word")}: Delete an word from the word list.
"""


# ------------- Working with files:
def read_file():
    with open('./data', 'r', encoding='utf-8') as f:
        data = f.read()
        res = ast.literal_eval(data)
    return res

def modify_file(value, path1, path2):
    new_file = read_file() #dictionary
    new_file[path1][path2] = value
    with open('./data', 'w', encoding='utf8') as f:
        f.write(str(new_file))

# ------------- Strings
def normalize(s): # It removes the accents of a string
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

# ------------- Config:
def get_config(message, error_message, option1, option2, path):
    option1 = option1.lower()
    option2 = option2.lower()
    
    setting = input(message).lower()
    while setting != option1 and setting != option2:
        setting = input(error_message).lower()
        
    if setting == option1:
        modify_file(option1, "user_info", path)
    elif setting == option2:
        modify_file(option2, "user_info", path)


def config():
    print("Hangman Game Settings")
    get_config("Select an operative system (win10 or unix): ", f"Select {color('red', 'a valid')} operative system: (Write {color('bold', 'win10')} or {color('bold', 'unix')}): ", "win10", "unix", "operative_system")
    get_config("Select a language for play (EN or ES): ", f"Select {color('red', 'a valid')} language: (Write {color('bold', 'EN')} or {color('bold', 'ES')}): ", "EN", "ES", "language")
    print(f"successful Finished Hangman settings, to modify the word list use {color('bold', 'hangman -l')}")


# ------------- Play:
def getWord(language):
    language = language.lower()
    file = read_file()
    word_list = file["word_list"][language]
    i = random.randint(0, len(word_list) - 1)

    word = word_list[i]
    return word

def play():
    updateScreen(0)

def updateScreen(hangman_state):
    operative_system = read_file()['user_info']['operative_system']
    if operative_system == 'win10':
        os.system('cls')
    elif operative_system == 'unix':
        os.system('clear')

    line = ''
    i = 0
    while i < TERMINAL_SIZE.columns:
        line += '-'
        i += 1
    print(line)

    if columns < 32:
        title_size = 13
        title = 'H A N G M A N'
    elif columns < 65:
        title_size = 31
        title = SMALL_TITLE
    else:
        title_size = 62
        title = HANGMAN_TITLE

    row1_margin = int((columns - title_size) / 2) * " "
    for line in title.splitlines():
        print(row1_margin + line)

    i = 0
    word = getWord('EN')
    row2_margin = int(columns - (9 + len(word) * 4) / 2) * " "
    for line in HANGMAN_PICS[hangman_state].splitlines():
        if i == 50:
            print((row2_margin * 4) + line + row2_margin + ("--- " * len(word)))
        else:
            print((row2_margin * 4) + line)
        i += 1



def list():
    pass

def add_word(word):
    stringNormalized = normalize(word).lower().split()
    stringNormalized = stringNormalized[0]

    if len(stringNormalized) <= 3:
        return print(color('red', 'Error: ') + '"' + stringNormalized + '" is a very short word (min length 4 characters)')

    if stringNormalized != word:
        bold = 'bold'
        response = input(f'Want add the word "{color(bold, stringNormalized)}"? (yes, no): ')
        if response.lower() != 'yes':
            return print("Word was not added")

    language = input(f'Language: (en or es): ').lower()
    while language != 'en' and language != 'es':
        language = input(color('red', 'Select a valid language ') + '(' + color('bold', 'en') + ' or ' + color('bold', 'es') + '): ').lower()
    
    file = read_file()
    old_word_list = file["word_list"][language]
    new_word_list = old_word_list + [stringNormalized]
    modify_file(new_word_list, 'word_list', language)
    print('Word "' + color('bold', stringNormalized) + '" was added successfully to the "' + language + '" word list')

def delete_word(word):
    print("SE ELIMINO LA palabra", word)


# ------------- Program:
def read_args():
    arguments = sys.argv
    arguments.pop(0)

    if len(arguments) > 2:
        return print(f"{color('red', 'Error: So many arguments used.')} We recommend using use {color('bold', 'hangman -h')}")

    if arguments == []:
        return print(help_message)
    elif "-h" in arguments:
        return print(help_message)
    elif "-c" in arguments:
        return config()
    elif "-p" in arguments:
        return play()
    elif "-l" in arguments:
        return list()
    elif "-a" in arguments:
        if len(arguments) == 1:
            print(color('red', 'Error: ') + 'Please enter a word. (hangman -a word)')
        else:
            return add_word(arguments[1])
    elif "-d" in arguments:
        return delete_word(arguments[1])

def run():
    read_args()

if __name__ == '__main__':
    run()