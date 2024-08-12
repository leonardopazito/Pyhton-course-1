# Password Generator Project

import random
import data

# Defining characteres
letters = data.letters
symbols = data.symbols
numbers = data.numbers


def generator_password(nr_letters: int = 0,
                       nr_symbols: int = 0,
                       nr_numbers: int = 0) -> str:
    """Generate a password with nr_letters letters, nr_symbols symbols and
    nr_numbers numbers.

    Args:
        nr_letters (int, optional): number of letters. Defaults to 0.
        nr_symbols (int, optional): number of symbols. Defaults to 0.
        nr_numbers (int, optional): number of numbers. Defaults to 0.

    Returns:
        str: Generated password
    """
    # letters - random list
    list_of_random_letters = [letters[random.randint(0, len(letters)-1)]
                              for _ in range(0, nr_letters)]

    # symbols - random list
    list_of_random_symbols = [symbols[random.randint(0, len(symbols)-1)]
                              for _ in range(0, nr_symbols)]

    # numbers - random list
    list_of_random_numbers = [numbers[random.randint(0, len(numbers)-1)]
                              for _ in range(0, nr_numbers)]

    # All characteres of password
    characters_of_password = [*list_of_random_letters,
                              *list_of_random_numbers,
                              *list_of_random_symbols]

    # shuffle of characteres of password
    random.shuffle(characters_of_password)

    password = ''.join(characters_of_password)
    return password


print(generator_password(1, 2, 3))
