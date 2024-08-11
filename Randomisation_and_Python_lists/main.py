import random
from options_ import rock, paper, scissors


possible_choices_format = [paper, rock, scissors]
"""0 = paper, 1 = rock and 2 = scissors"""

RULES_OF_GAME = [{0: 1},
                 {1: 2},
                 {2: 0}]
"""key wins of RULES_OF_GAME[key]"""

is_game = True
while is_game:
    print("Welcome to Rock Paper Scissors Game")

    valid = False
    while not valid:
        try:
            your_chose = int(
                input("Type 0 for paper, 1 for rock or 2 for Scissors: "))
        except ValueError:
            print('Choose invalid.')
        else:
            if your_chose in [0, 1, 2]:
                valid = True
            else:
                print("Invalid number")

    computer_chose = random.randint(0, 2)
    print("\n")
    print("Computer chose:")
    print(possible_choices_format[computer_chose])

    print("Your chose")
    print(possible_choices_format[your_chose])

    if {your_chose: computer_chose} in RULES_OF_GAME:
        print("You won")
    elif {computer_chose: your_chose} in RULES_OF_GAME:
        print('Computer won')
    else:
        print("Nobody won.")

    if not "s" == input("Type s to play again or q to end:\n").lower():
        is_game = False
