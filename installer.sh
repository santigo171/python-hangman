#!/bin/bash
path=$(pwd)

echo "Hangman game by David Hurtado will be installed in this folder "$path"/hangman_game/"
echo "To start installing press enter"
echo "To cancel press ctrl + z and then go to the folder you want to install."
echo "Version: 1.0"
read x

mkdir hangman_game
cd hangman_game
path=$(pwd)

curl https://raw.githubusercontent.com/santigo171/python-hangman/main/main.py > main.py
curl https://raw.githubusercontent.com/santigo171/python-hangman/main/data > data
data_path="$path/data"

# sed -i -e 's/pattern_to_search/text_to_replace/' file.txt
sed -i -e 's,DATA_PATH,'$data_path',g' main.py

# sed s,DATA_PATH,$data_path,g main.py > main.py
cd /home/$USER
cat .bashrc > .bashrc_copy
echo 'alias hangman="python3 '$path'/main.py"' >> .bashrc
echo "Succefully installed Hangman Game by David Hurtado, remember have python3 installed too."
echo "Please restart the terminal. Then, start playing with 'hangman' command."