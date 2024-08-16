# ############### Coffee Machine ######################
from menu import (MENU, resources)
from os import system


# ------- Functions ---------

def print_report(money_in_the_machine: float,
                 my_resources: dict[str, int]) -> None:
    """Print the actual resources and the money in the machine"""

    for item in my_resources.keys():
        print(f"{item}: {my_resources[item]}")
    print(f"Money: ${money_in_the_machine}")


def make_drink(drink: str, my_resources: dict[str, int]) -> None:
    """Make the drink and updates the resources of the coffe machine."""

    try:
        for ingredient in MENU[drink]['ingredients']:
            my_resources[ingredient] -= MENU[drink]['ingredients'][ingredient]
    except KeyError:
        print(f"The {drink} is not available.")


def is_there_resources_sufficient(item: str,
                                  my_resources: dict[str, int]) -> bool:
    """Check if the resources is sufficient to prepare the item"""
    for ingredient in MENU[item]['ingredients']:
        if MENU[item]['ingredients'][ingredient] > my_resources[ingredient]:
            print(f'Sorry, there is not enough {ingredient}!.')
            return False
    return True


def process_coins(drink: str) -> float:
    """Receives money from the user and processes it."""

    print(f"The {drink} cost {MENU[drink]['cost']}")
    total = 0
    coins_types = ['Quarter ($0.25): ',
                   'Dimes ($0.10): ',
                   'Nickles ($0.05): ',
                   'Pennies ($0.01): ']
    coins_value = [0.25, 0.10, 0.05, 0.1]

    for index, coin in enumerate(coins_types):
        total += coins_value[index] * int(input(coin))
        system('clear')
        print(f"Total: {total} \n")
        if MENU[drink]['cost'] - total <= 0:
            return total
        else:
            print(f"Missing quantity: {round(MENU[drink]['cost'] - total, 2)}")
    return total


def coffe_machine_turn_on():

    should_continue = True
    money = 0
    actual_resources = resources

    while should_continue:
        new_choice = True
        while new_choice:
            drink_ch_msg = "What would you like ? (espresso/latte/cappuccino) "
            drink_choice = input(drink_ch_msg).lower()
            system('clear')

            is_the_choice_a_coffee = drink_choice in MENU.keys()
            if is_the_choice_a_coffee:
                new_choice = False
            elif drink_choice == 'off':
                should_continue = False
                new_choice = False
            elif drink_choice == "report":
                print_report(money, actual_resources)

        if should_continue:
            if is_there_resources_sufficient(drink_choice, actual_resources):
                cost = MENU[drink_choice]['cost']
                total_insert = process_coins(drink_choice)

                if total_insert < cost:
                    print("Sorry that's not enough money. Money refunded")
                    print(f'Total: {round(total_insert, 2)}.'
                          f'The {drink_choice} cost ${cost}')
                    print('\n')
                else:
                    money += cost
                    print("--- Machine report ---")
                    print_report(money, actual_resources)
                    print("\n")

                    if total_insert > cost:
                        change = total_insert - cost
                        print("---- Return ----")
                        print(f"Here is ${round(change, 2)} dollars in change")
                        make_drink(drink_choice, actual_resources)
                        print(f"Here is your {drink_choice}. Enjoy!")
            continue_msg = 'Should continue: "y" or "n": '
            should_continue = input(continue_msg).lower() == 'y'
            system('clear')


coffe_machine_turn_on()
