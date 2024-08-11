import random
import os
from hangman_art import logo, stages
import hangman_words

word_list = hangman_words.word_list


chosen_word = random.choice(word_list)
chosen_word_list = [letter for letter in chosen_word]
LIVES = 6
actual_live = LIVES
wrong_letters = ''

# Logo
print(logo)

# Exclude this line in the final project
print(f"Test: The solution is {chosen_word}")

# Create blanks
display = ["_" for letter in chosen_word]


def update_lives(display_: list[str], letter: str, lives: int) -> None:
    """It updates the numbers of lives remaining

    Args:
        display (str): Actual display that will be analyzed
        letter (str): Chosen letter
        lives (int): Actual number of lives
    """
    global actual_live, wrong_letters
    if letter not in display_:
        actual_live -= 1
        if actual_live < LIVES - 1:
            wrong_letters += ", "+letter
        elif actual_live == LIVES - 1:
            wrong_letters += letter
        else:
            wrong_letters = wrong_letters


guess = input('Guess a letter: ').lower()
while (not display == chosen_word_list) and (actual_live >= 0):

    # Check guessed letter
    word_lenght = len(chosen_word)
    display = [guess if letter == guess
               else display[position]
               for position, letter in enumerate(chosen_word)]

    update_lives(display, guess, actual_live)

    if actual_live == -1:
        print('You lose!')
    else:
        print(stages[actual_live])
        print(f"{' '.join(display)}")
        print(f"Wrong choices: {wrong_letters}")
        print(f"Lives: {actual_live}")
        print()
        guess = input('Guess a letter: ').lower()
        os.system('clear')
        # Logo
        print(logo)


if display == chosen_word_list:
    print('You Won!')
