"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    counter = INITIAL_GUESSES
    guess_word = ['-'] * len(secret_word)
    
    while counter > 0:
        print_word(guess_word)
        guess = input("Type a single letter here, then press enter: ")
        print(f"You have {counter} guesses left")
        
        if guess in secret_word:
            fill_guess_word(secret_word, guess_word, guess)
            print("That guess is correct.")
        elif guess_word == secret_word:
            print(f"Congratulations, the word is: {secret_word}")
            break
        else:
            counter -= 1
    print(f"Sorry, you lost. The secret word was: {secret_word}")
        
def fill_guess_word(secret_word, guess_word, guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            guess_word[i] = guess
            
def print_word(word):
    print("The word now looks like this: ", "".join(word))
    

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    with open(LEXICON_FILE, 'r') as file:
        word_list = [line.strip() for line in file.readlines()]
    return random.choice(word_list)


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()