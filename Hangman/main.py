import random
import os
from hangman_art import logo, stages
import hangman_words

word_list = hangman_words.word_list


chosen_word = random.choice(word_list)
chosen_word_list = [letter for letter in chosen_word]
lives = 6
actual_live = lives
wrong_letters = ''

# Logo
print(logo)

# Testing code
print(f"Test: The solution is {chosen_word}")

# Create blanks
display = ["_" for letter in chosen_word]


guess = input('Guess a letter: ').lower()
while (not display == chosen_word_list) and (actual_live >= 0):

    # Check guessed letter
    word_lenght = len(chosen_word)
    for position in range(word_lenght):
        if guess == chosen_word[position]:
            display[position] = guess

    if guess not in display:
        actual_live -= 1
        if actual_live < lives - 1:
            wrong_letters += ", "+guess
        elif actual_live == lives - 1:
            wrong_letters += guess
        else:
            wrong_letters = wrong_letters

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
