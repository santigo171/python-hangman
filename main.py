import time
import os
import random
import sys

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

HANGMAN_PICS = ['''
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

# ------------- Colors:
def color(color, string):
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
{color('bold', "hangman -s")}: Show some user stats.

{color('bold', "hangman -l")}: Show the word list.
{color('bold', "hangman -a word")}: Add an word to the word list.
{color('bold', "hangman -d word")}: Delete an word from the word list.
"""


# ------------- Working with files:
def read_file(path):
    pass

def modify_file(path, value):
    pass

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
    setting = input(message)
    while setting != option1 and setting != option2:
        setting = input(error_message)
    
    if setting == option1:
        modify_file(f"[user_info][{path}]", option1)
    elif setting == option2:
        modify_file(f"[user_info][{path}]", option2)


def config():
    print("Hangman Game Settings")
    get_config("Select an operative system (win10 or unix): ", f"Select {color('red', 'a valid')} operative system: (Write {color('bold', 'win10')} or {color('bold', 'unix')}): ", "win10", "unix", "operative_system")
    
    get_config("\nSelect a language for play (EN or ES): ", f"Select {color('red', 'a valid')} language: (Write {color('bold', 'EN')} or {color('bold', 'ES')}): ", "EN", "ES", "language")

    print(f"successful Finished Hangman settings, to modify the word list use {color('bold', 'hangman -l')}")


# ------------- Play:
def play():
    while True:
        updateScreen()
        time.sleep(1)
    

def updateScreen():
    os.system('clear')

    line = ''
    i = 0
    while i < TERMINAL_SIZE.columns:
        line += '-'
        i += 1
    print(line)

    if columns < 65:
        pass
    else:
        row1_margin_value = (columns - 62) / 2
        row1_margin = int(row1_margin_value) * " "
        for line in HANGMAN_TITLE.splitlines():
            print(row1_margin + line)



def stats():
    print("MOMENTO Stats")


def list():
    print("MOMENTO LIST")

def addWord(word):
    print("SE AGREGO LA palabra", word)

def deleteWord(word):
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
    elif "-s" in arguments:
        return stats()
    elif "-l" in arguments:
        return list()
    elif "-a" in arguments:
        return addWord(arguments[1])
    elif "-d" in arguments:
        return deleteWord(arguments[1])

def run():
    read_args()

if __name__ == '__main__':
    run()