# WordleBot

WordleBot is a Python-based program that allows users to find the most optimal moves to a variant of the popular word puzzle game Wordle. In this version, the bot will guess a 6-letter word based on clues about the presence and position of each letter. The program was created by Pratham Mehta and was inspired by 3Blue1Brown.

## Getting Started

To get started with WordleBot, you will need to install the dependencies listed in the `requirement.txt` file using `pip`. Once the dependencies are installed, you can run the program by executing the `gui.py` file. This will launch a graphical interface built with `tkinter`.

## How to Play

To play WordleBot, enter each letter of your guess into the 6 letter boxes at the top of the interface. You can use the space bar to jump between the boxes. For example: `d` - `e` - `t` - `a` - `i` - `l`. Once you have entered your guess, press the enter key to submit it.

Next, you must give the program information about your word by typing '`g`' for letters that are green, '`y`' for letters that are yellow, and '`n`' for letters that are not present in the word. For example, if the word "detail" is colored `green` - `yellow` - `nothing` - `nothing` - `yellow`, you would type `gynny`.

The program will then process your information and display a list of possible words in the right-hand column, sorted by their probability based on the information you provided and their frequency in the English language. You can then repeat this process until you successfully guess the word.

## Credits

- Pratham Mehta: Creator of WordleBot
- 3Blue1Brown: Inspiration for WordleBot

