""" Possible future features:

hangman -l:
    filter by:
        alphabetical order
        recently added
hangman -p:
    animations
"""

import os #to clear screen
import sys #to get arguments
import ast # String to dic
import random 
from random import randint

TERMINAL_SIZE = os.get_terminal_size()
columns = TERMINAL_SIZE.columns
rows = TERMINAL_SIZE.lines
VERSION = "1.0"
forbidden = ["_", "-", "\\", "/", "|", "+", "*", "{", "}", "[", "]", "=", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "‏", "@", "!", ",", ".", ";", ":", "#", "$", "%", "^", "&", "~", "`", "?", "'"]

# ------------- Sprites:
HANGMAN_TITLE = """██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                    by David Hurtado"""

SMALL_TITLE = """█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█
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

WIN_MESSAGE = '''        o    .   _     .
          .     (_)         o
   o      ____            _       o
  _   ,-/   /)))  .   o  (_)   .
 (_)  \_\  ( e(     O             _
 o       \/' _/   ,_ ,  o   o    (_)
  . O    _/ (_   / _/      .  ,        o
     o8o/    \\_/ / ,-.  ,oO8/( -TT
    o8o8O | } }  / /   \Oo8OOo8Oo||     O
   Oo(""o8"""""""""""""""8oo""""""")
  _   `\`'                  `'   /'   o
 (_)    \                       /    _   .
      O  \           _         /    (_)
o   .     `-. .----<(o)_--. .-'
   --------(_/------(_<_/--\_)-----------
'''

LOSE_MESSAGE = """                             Z             
                       Z                   
        .,.,        z           
      (((((())    z             
     ((('_  _`) '               
     ((G   \\  |)                 
    (((`   " ,                  
     .((\.:~:          .--------------.    
     __.| `"'.__      | \\              |     
  .~~   `---'   ~.    |  .             :     
 /                `   |   `-.__________)     
|             ~       |  :             :   
|                     |  :  |              
|    _                |     |   [ ##   :   
 \\    ~~-.            |  ,   oo_______.'   
  `_   ( \) _____/~~~~ `--___              
"""

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
    'm': '╔╗╗\n║║║',
    'n': '▄▄▄\n█ █',
    'o': '█▀█\n█▄█',
    'p': '█▀█\n█▀▀',
    'q': '█▀█\n▀▀█',
    'r': '█▀█\n█▀▄',
    's': '█▀░\n▄█░',
    't': '▀█▀\n░█░',
    'u': '█░█\n█▄█',
    'v': '█░█\n▀▄▀',
    'w': '║║║\n╚╝╝',
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

help_message = f"""{color('bold', "HANGMAN Game, created by David Hurtado")} {color('blue', "@santigo171.")}
Version: {VERSION}
This is an open source project: https://github.com/santigo171/python-hangman

{color('bold', "hangman -p")}: Play an Hangman Game.

{color('bold', "hangman -h")}: Show the help message.
{color('bold', "hangman -c")}: Will make some config changes.

{color('bold', "hangman -l language")}: Show the word list.
{color('bold', "hangman -a language word")}: Add an word to the word list.
{color('bold', "hangman -d language word")}: Delete an word from the word list."""

# ------------- Working with files:
data_path = 'DATA_PATH'
# IMPORTANT: The word DATA_PATH is remplaced by the file path on the installation
def read_file():
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = f.read()
            res = ast.literal_eval(data)
        return res
    except (TypeError, NameError, SyntaxError, FileNotFoundError):
        print(f"{color('red', 'Error:')} Can't find the file named 'data', we are restoring the file, but please, don't modify or delete that file...")
        restore_file()
        print("File restored!, please make an 'hangman -c' to configure again the game.")
        quit()


def modify_file(value, path1, path2):
    new_file = read_file() #dictionary
    new_file[path1][path2] = value
    with open(data_path, 'w', encoding='utf8') as f:
        f.write(str(new_file))

def restore_file():
    new_file = "{'user_info': {'operative_system': 'unix', 'language': 'es'}, 'word_list': {'es': ['velociraptor', 'ganar', 'golpear', 'caramelos', 'espeso', 'esposo', 'ancho', 'lavanderia', 'babear', 'twitter', 'prisionera', 'indiferentemente', 'imaginar', 'reconocer', 'zodiaco', 'popular', 'sentado', 'seco', 'calcio', 'bomba', 'humano', 'grabador', 'pintura', 'cucaracha', 'abrazadera', 'espiral', 'embarazo', 'cueva', 'remolacha', 'satelite', 'bache', 'desenvolver', 'reprobar', 'dirigir', 'bateria', 'calzado', 'aplastar', 'moverse', 'murmurar', 'cancha', 'reina', 'claustrofobia', 'farmacia', 'ventana', 'estallido', 'terraza', 'desnudarse', 'retorcer', 'perfume', 'coleccion', 'torre', 'rata', 'vestuario', 'microondas', 'operacion', 'dichoso', 'aparatos', 'historiador', 'boleto', 'provincia', 'hormiga', 'flecha', 'lanzallamas', 'observatorio', 'ventilador', 'holanda', 'escenario', 'fotografiar', 'sismo', 'roto', 'fregadero', 'trineo', 'nuez', 'aletear', 'sintonizar', 'desviar', 'mayordomo', 'rianchuelo', 'museo', 'restaurante', 'mangas', 'magnetico', 'probar', 'regar', 'pelo', 'cuero', 'ascendiente', 'tanga', 'dinamarca', 'mariquita', 'circuito', 'veredicto', 'sinusitis', 'blusa', 'calendario', 'atracar', 'barranco', 'peste', 'asustar', 'untar', 'embudo', 'chicos', 'mantel', 'escribir', 'respirador', 'micro', 'cerebro', 'lastimar', 'colectivo', 'almendra', 'derecha', 'alarma', 'memoria', 'gente', 'punta', 'aperitivo', 'archivo', 'existente', 'capitulo', 'prima', 'desaparecido', 'sabor', 'estimar', 'arcano', 'vibora', 'capturado', 'lesion', 'auxiliar', 'desercion', 'completamente', 'doble', 'ayuda', 'mejor', 'labios', 'ardiente', 'alfabetico', 'cocinero', 'grunidos', 'sanguijuela', 'rojo', 'trebol', 'palanca', 'mando', 'vuelta', 'caracol', 'pueblo', 'besos', 'mision', 'fachada', 'destello', 'hiedra', 'ausencia', 'jefe', 'arma', 'fuego', 'perro', 'piezas', 'desesperacion', 'traicion', 'final', 'erupcion', 'absolucion', 'perezoso', 'surgir', 'franqueza', 'ahogo', 'diabolico', 'algunos', 'grava', 'abrazo', 'oriental', 'papi', 'emboscada', 'bolso', 'horrendo', 'aspero', 'subterraneo', 'secuestrado', 'coartada', 'imperio', 'enigma', 'ladron', 'homicidio', 'cena', 'piramides', 'atmosfera', 'caballos', 'caracteristica', 'carnicero', 'chocar', 'canela', 'cangilon', 'cincel', 'destruir', 'asombroso', 'brutalmente', 'grande', 'usable', 'sabiduria', 'cena', 'cuna', 'lamer', 'libertinaje', 'leyenda', 'picadillo', 'colina', 'bicicleta', 'zumbido', 'nudillos', 'continuo', 'faraon', 'granito', 'destileria', 'verdugo', 'traficante', 'temeroso', 'toro', 'desolado', 'repeticion', 'llave', 'gigantesco', 'flotar', 'dominante', 'duque', 'collar', 'chiflado', 'moda', 'robotico', 'exacto', 'corpulento', 'angustia', 'parachoque', 'atras', 'posicion', 'eliminacion', 'grabar', 'cera', 'huerta', 'bosque', 'medio', 'camino', 'corral', 'futuro', 'nuevo', 'animalista', 'devastacion', 'dulce', 'dinosaurio', 'locura', 'piedra', 'terror', 'cierto', 'arcilla', 'emitir', 'ciudad', 'nudo', 'caida', 'heroico', 'ataud', 'vida', 'definitivo', 'pobre', 'embriagante', 'pistola', 'rapido', 'natural', 'arriesgado', 'descripcion', 'terminar', 'sabotaje', 'escarcha', 'gases', 'lacrimogeno', 'rapido', 'tormenta', 'nieve', 'personal', 'sistema', 'objeto', 'feudal', 'talon', 'crema', 'cafe', 'estrella', 'explosion', 'guitarra', 'plastico', 'navaja', 'martillo', 'libros', 'lapiz', 'lapicera', 'aluminio', 'embarcacion', 'letra', 'agujeta', 'libreria', 'sonido', 'universidad', 'rueda', 'llaves', 'camisa', 'papa', 'sillon', 'felicidad', 'catre', 'teclado', 'servilleta', 'escuela', 'pantalla', 'codo', 'tenedor', 'estadistica', 'mapa', 'agua', 'mensaje', 'lima', 'cohete', 'edificio', 'cesped', 'presidencia', 'hojas', 'parlante', 'colegio', 'granizo', 'pestana', 'lampara', 'mano', 'monitor', 'flor', 'musica', 'hombre', 'tornillo', 'habitacion', 'velero', 'abuela', 'abuelo', 'palo', 'templo', 'lentes', 'boligrafo', 'plato', 'nube', 'gobierno', 'botella', 'castillo', 'enano', 'casa', 'libro', 'persona', 'planeta', 'televisor', 'guantes', 'metal', 'telefono', 'proyector', 'mono', 'remera', 'muela', 'petroleo', 'percha', 'remate', 'debate', 'anillo', 'cuaderno', 'ruido', 'pared', 'taladro', 'herramienta', 'cartas', 'chocolate', 'anteojos', 'impresora', 'living', 'luces', 'zapato', 'lluvia', 'corbata', 'periodico', 'diente', 'planta', 'chupetin', 'buzo', 'oficina', 'persiana', 'puerta', 'silla', 'ensalada', 'pradera', 'zoologico', 'candidato', 'deporte', 'recipiente', 'diarios', 'fotografia', 'hierro', 'refugio', 'pantalon', 'barco', 'carne', 'tecla', 'humedad', 'departamento', 'celular', 'tristeza', 'hipopotamo', 'sofa', 'cama', 'arbol', 'mesada', 'campera', 'discurso', 'auto', 'cinturon', 'rucula', 'famoso', 'madera', 'lentejas', 'piso', 'maletin', 'reloj', 'diputado', 'cuchillo', 'desodorante', 'candado', 'montanas', 'computadora', 'radio', 'mono', 'cuadro', 'calor', 'partido', 'teatro', 'fiesta', 'bala', 'auriculares'], 'en': ['crude', 'lawn', 'broadcaster', 'horizon', 'lamp', 'tooth', 'secret', 'meeting', 'antiquity', 'president', 'successfully', 'chicken', 'convince', 'architect', 'redeem', 'favorable', 'excavate', 'execution', 'embarrassment', 'queen', 'synchronous', 'limited', 'superintendent', 'expectation', 'defend', 'document', 'rational', 'weapon', 'respect', 'mastermind', 'generation', 'claim', 'aluminium', 'risk', 'baboon', 'badger', 'bear', 'beaver', 'camel', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'donkey', 'duck', 'eagle', 'ferret', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra', 'complete', 'prefer', 'stage', 'lace', 'touch', 'wood', 'whine', 'cheese', 'thin', 'weight', 'bless', 'ethereal', 'read', 'rampant', 'defeated', 'peel', 'nervous', 'cooing', 'attack', 'furtive', 'flame', 'gamy', 'adorable', 'boat', 'reading', 'ready', 'malicious', 'screw', 'robin', 'insurance', 'decision', 'guide', 'pumped', 'economic', 'question', 'vanish', 'married', 'kick', 'montainous', 'waggish', 'kiss', 'animated', 'cent', 'ground', 'trap', 'evasive', 'vague', 'unaccountable', 'sneeze', 'middle', 'daughter', 'fascinated', 'juicy', 'decide', 'degree', 'precede', 'bleach', 'floor', 'billowy', 'agreement', 'continue', 'spicy', 'perform', 'bird', 'dream', 'detect', 'courageous', 'guady', 'absorbing', 'welcome', 'foolish', 'minute', 'scatter', 'envious', 'fortunate', 'furniture', 'spiders', 'efficient', 'kitty', 'steam', 'mice', 'hill', 'meaty', 'yummy', 'apathetic', 'discreet', 'borrow', 'drum', 'helpful', 'trade', 'violet', 'enchanted', 'lame', 'fertile', 'cruel', 'edge', 'reject', 'talk', 'cloth', 'undress', 'unwieldy', 'toys', 'yard', 'seat', 'show', 'modern', 'flashy', 'volatile', 'sisters', 'rainstorm', 'colour', 'meddle', 'adaptable', 'poke', 'slow', 'sleep', 'violent', 'color', 'placid', 'dangerous', 'obscene', 'unsuitable', 'young', 'market', 'screeching', 'market', 'absurd', 'cooperative', 'noiseless', 'uppity', 'desing', 'boiling', 'stove', 'simple', 'fast', 'phone', 'confused', 'overrated', 'order', 'grin', 'cluttered', 'home', 'drink', 'profuse', 'sincere', 'smile', 'minor', 'cakes', 'flowery', 'deserve', 'hideous', 'mine', 'bang', 'print', 'infamous', 'snobbish', 'miscreant', 'needle', 'tomatoes', 'position', 'able', 'milk', 'channel', 'switch', 'station', 'steady', 'basket', 'helpless', 'addition', 'scrape']}}"
    file = open(data_path, "w")
    file.write(new_file)
    file.close()

# ------------- Strings
def normalize(s): # It removes the accents of a string
    replacements = [
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
        ('"', "")
    ]

    for letter in forbidden:
        tuple = (letter, '')
        replacements.append(tuple)

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
    try:
        print("Hangman Game Settings")
        get_config("Select an operative system (win10 or unix): ", f"Select {color('red', 'a valid')} operative system: (Write {color('bold', 'win10')} or {color('bold', 'unix')}): ", "win10", "unix", "operative_system")
        get_config("Select a language for play (EN or ES): ", f"Select {color('red', 'a valid')} language: (Write {color('bold', 'EN')} or {color('bold', 'ES')}): ", "EN", "ES", "language")
        print(f"successful Finished Hangman settings, to modify the word list use {color('bold', 'hangman -l')}")
    except KeyboardInterrupt:
        print(color('red', '\nError: ') + "KeyboardInterrupt, please use 'hangman -c' again to save changes.")

# ------------- Play:
def getWord(language):
    language = language.lower()
    file = read_file()
    word_list = file["word_list"][language]
    i = random.randint(0, len(word_list) - 1)

    word = word_list[i]
    return word

def play():
    # Default:
    language = read_file()['user_info']['language']
    word = getWord(language)
    
    true_letters = [{'hit': True, 'letter': char} for char in word] 
    hit_letters = [{'hit': False, 'letter': char} for char in word]
    user_input_list = []
    hangman_state = 0
    won = False
    error = ''

    updateScreen(hangman_state, word, hit_letters, language, error)

    while hangman_state < 6 or won == False:
        updateScreen(hangman_state, word, hit_letters, language, error)
        forbidden_character = False
        already_guessed = False
        user_input = input("Guess: ")
        user_input = user_input.lower()

        for letter in forbidden:
            if user_input == letter:
                forbidden_character = True
                break

        normalized_user_input = normalize(user_input)
        
        for letter in user_input_list:
            if letter == normalized_user_input:
                already_guessed = True

        if len(user_input) > 1:
            error = "Please enter only ONE letter"
        elif len(user_input) == 0:
            error = "Please enter a letter"
        elif forbidden_character:
            error = f"'{user_input}' is not a valid letter."
        elif already_guessed:
            error = 'Already guessed "' + normalized_user_input + '"   '
        else:
            user_input_list.append(normalized_user_input)
            error = ''

        if error == '':
            i = 0
            add_hangman_state = True

            for dic in hit_letters:
                i+= 1
                if dic["letter"] == user_input:
                    dic["hit"] = True
                    add_hangman_state = False
                else:
                    if len(hit_letters) == i and add_hangman_state:
                        hangman_state += 1

        if hangman_state == 6:
            updateScreen(hangman_state, word, hit_letters, language, error)
            break
        elif hit_letters == true_letters:
            updateScreen(hangman_state, word, hit_letters, language, error)
            won = True
            break

    if won == True:
        final_message(True, f"LET'S GO!!! You won with the word {word}")
    elif won == False:
        final_message(False, f"Umm you lost ¯\(°_o)/¯, the word was {word}")
    return

def final_message(won, message):
    if won == True:
        asset = WIN_MESSAGE
    elif won == False:
        asset = LOSE_MESSAGE

    if columns > 40:
        margin = int((columns -  41) / 2) * " "
        for line in asset.splitlines():
            print(margin + line)
        print(margin + color('bold', message))
    else:
        print(color('bold', message))

def updateScreen(hangman_state, word, hit_letters, language, error):
    # Clean screen and warn about the OS
    print(color('bold', color('yellow', 'Warning: ') + 'You should make a "hangman -c" to set your operative system.'))
    operative_system = read_file()['user_info']['operative_system']
    if operative_system == 'win10':
        os.system('cls')
    elif operative_system == 'unix':
        os.system('clear')

    # BIG PRO LINE
    line = ''
    i = 0
    while i < columns:
        line += '-'
        i += 1
    print(line)

    # BIG "or small" pro title
    if columns < 32:
        title = 'H A N G M A N'
        word_size = 1
    elif columns < 68:
        title = SMALL_TITLE
        word_size = 1
    else:
        title = HANGMAN_TITLE
        word_size = 3

    title_size = len(title.splitlines()[0])

    row1_margin = int((columns - title_size) / 2) * " "
    for line in title.splitlines():
        print(row1_margin + line)

    i = 0
    # calc margins and lines
    content_size = 9 + (len(word) * (word_size + 1)) + 5
    row2_margin = int((columns -  content_size) / 2) * " "
    
    margin = "     "
    row2_3 = margin[1:-1] + " "
    row2_4 = margin[1:-1] + " "
    row2_5 = margin + (len(word) * (word_size * "-" + " "))
    
    print("\n")

    # Put into each line the letters of the word:
    try:
        for letter_dic in hit_letters:
            if letter_dic["hit"]: # THE PLAYER SAID THE LETTER!!!!
                if columns < 68:    # Small letters
                    row2_4 += " " + letter_dic["letter"].swapcase()
                else:               # BIG LETTER BOI LETS GOOOOOO
                    letter = letter_dic["letter"]
                    row2_4 += " " + alphabet[letter].splitlines()[1]
                    row2_3 += " " + alphabet[letter].splitlines()[0]

            else:                 # THE PLAYER DIDN'T SAID THE LETTER :(
                if columns < 68:
                    row2_4 += "  "
                else:
                    row2_4 += " " + "   "
                    row2_3 += " " + "   "
    except KeyError:
        command = color('bold', 'hangman -d ' + language + " " + word)
        return print(f"\n{color('red', 'Error: ')} the word: {color('bold', word)} from the {color('bold', language)} dictionary have invalid characters. Please make an {command} And then, if you want, add it again with only alphabet characters (A - Z) NOT NUMBERS OR SYMBOLS.")

    # print all lets gooooooooo
    for pic in HANGMAN_PICS[hangman_state].splitlines():
        if i == 3:
            print(row2_margin + pic + row2_3)
        elif i == 4:
            print(row2_margin + pic + row2_4)
        elif i == 5:
            print(row2_margin + pic + row2_5)
        else:
            print(row2_margin + pic)
        i += 1
    if error != '':
        print(color('red', "Error: ") + error)
    else:
        print()


def list(language):
    file = read_file()

    language = language.lower()
    while language != 'en' and language != 'es':
        language = input("Please enter a valid language (en or es): ")

    if language == 'en':
        print(color("bold", "English:"))
    if language == 'es':
        print(color("bold", "Spanish:"))

    word_list = file["word_list"][language]
    for word in word_list:
        print(f"{word_list.index(word) + 1}. {word}")

def add_word(language, array_word):
    try:
        normalized_array_word = []
        for word in array_word:
            stringNormalized = normalize(word).lower()
            normalized_array_word.append(stringNormalized)
        
        language = language.lower()
        while language != 'en' and language != 'es':
            language = input("Please enter a valid language (en or es): ")

        file = read_file()
        old_word_list = file["word_list"][language]

        for old_word in old_word_list:
            for word in normalized_array_word:
                if word == old_word:
                    print(color('red', "Error: ") + word + " is already in the list. Word was not added.")
                    normalized_array_word.remove(word)

                if len(word) <= 3 or len(word) > 14:
                    print(color('red', 'Error: ') + '"' + word + '" is a very short or a very long word (min 4 characters, max 14 characters)')
                    normalized_array_word.remove(word)

        if array_word != normalized_array_word:
            word_list = ''
            for word in normalized_array_word:
                word_list += " " + word

            print("\nWant add the following words?" + word_list)
            response = input("(yes, no): ")
            if response.lower() != 'yes' and response.lower() != 'y':
                return print("Words were not added")

        new_word_list = old_word_list + normalized_array_word

        modify_file(new_word_list, 'word_list', language)
        print(f"{color('bold', word_list)} were added successfully to the {language} word list")
        
    except KeyboardInterrupt:
        print("\nWord was not added, Keyboard Interrupt.")

def delete_word(language, word):
    stringNormalized = normalize(word).lower().split()
    stringNormalized = stringNormalized[0]
    language = language.lower()

    while language != 'en' and language != 'es':
        language = input("Please enter a valid language (en or es): ")
    
    file = read_file()
    word_list = file["word_list"][language]
    try:
        word_list.remove(stringNormalized) 
    except ValueError:
        return print(color("red", "Error: ") + stringNormalized + " isn't in the '" + language + "' word list.")

    modify_file(word_list, 'word_list', language)
    print('Word "' + color('bold', stringNormalized) + '" was successfully deleted from the "' + language + '" word list')


# ------------- Program:
def read_args():
    arguments = sys.argv
    arguments.pop(0)

    if arguments == []:
        return print(help_message)

    elif "-h" in arguments:
        return print(help_message)

    elif "-c" in arguments:
        return config()

    elif "-p" in arguments:
        file = read_file()

        if len(file["word_list"]["es"]) <= 1 or len(file["word_list"]["en"]) <= 1:
            print(color('red', 'Error: '), 'There are not enough words to play.')

            answer = input('Want restore the word list with the default words? (y/n): ')

            if answer == 'yes' or answer == 'y':
                restore_file()
                print("Default words added! Use 'hangman -p' to play")
            else:
                print("Ok, the word list wasn't restored. But please, add your custom words with 'hangman -a'")
            return
        return play()

    elif "-l" in arguments:
        if len(arguments) == 1:
            print(color('red', 'Error: ') + 'Please enter a language. (hangman -l language)')
        else:
            return list(arguments[1])

    elif "-a" in arguments:
        if len(arguments) <= 2:
            print(color('red', 'Error: ') + 'Please enter a language and a word. (hangman -a language word word2 word3) (You can add has many words has you want after the language).')
        else:
            language = arguments[1]
            arguments.pop(0)
            arguments.pop(0)
            return add_word(language, arguments)

    elif "-d" in arguments:
        if len(arguments) <= 2:
            print(color('red', 'Error: ') + 'Please enter a language and a word. (hangman -d language word)')
        else:
            return delete_word(arguments[1], arguments[2])

    else:
        return print(color('red', 'Error') + ", can't find the argument " + str(arguments[0]) + f", We recommend using use {color('bold', 'hangman -h')}")

def run():
    try:
        read_args()
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')

if __name__ == '__main__':
    run()