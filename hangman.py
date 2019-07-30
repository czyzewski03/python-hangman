# Stop repeated guesses from reducing available guesses.


#!/usr/bin/env python

import random

def censor_word(word, ud_letters):
    """Replace all undiscovered letters in a word with underscores."""
    censored_word = []
    for char in word:
        if char in ud_letters:
            censored_word.append('_')
        else:
            censored_word.append(char)
    return ''.join(censored_word)

def validate_guess(guess):
    """Checks if the user's guess is valid."""
    if len(guess) > 1:
        return False
    elif not guess.isalpha():
        return False
    else:
        return True


with open('words.txt', 'r') as word_file:
    words = word_file.read() \
            .split(',')
            
guess_limit = 5
guessed_letters = set()
undiscovered_letters = set()

answer = random.choice(words)
remaining_guesses = guess_limit
undiscovered_letters = {char for char in answer if not char.isspace()}

print('Hangman\n')

while undiscovered_letters and remaining_guesses > 0:
    print(f'Guesses {remaining_guesses}/{guess_limit}')
    print(censor_word(answer, undiscovered_letters).upper())
    guess = input("Guess a letter: ").lower()

    if validate_guess(guess):

        # If a new letter has been guessed:
        if guess in undiscovered_letters:
            undiscovered_letters.remove(guess)
            guessed_letters.add(guess)
            print('Correct!')

        # If letter has already been guessed:
        elif guess in guessed_letters:
            print(f"'{guess}' has already been guessed")

        # If letter is incorrect:
        else:
            remaining_guesses -= 1
            guessed_letters.add(guess)
            print('Incorrect!')
    else:
        print(f"'{guess}' is not a valid guess")
    print('\n')

print(answer.upper())
if remaining_guesses:
    print('You win!')
else:
    print('You lose!')