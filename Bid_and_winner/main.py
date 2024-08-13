from art import logo
from os import system

restart = True
msg = "Are there any other bidders? Type 'yes' or 'no':"
ms1 = 'What is your name? '
ms2 = "What's your bid? $"

print("Welcome to the secret auction program.")
bidders = []


def add_bidders(name: str, bid_value: float) -> None:
    """Add bidders to list bidders

    Args:
        name (str): Name of bidder
        bid_value (float): Value of the bid
    """
    person = {}
    person["name"] = name
    person["bid"] = bid_value

    bidders.append(person)


def winner(list_of_bidders: list[dict]) -> dict:
    """Find the winner from list of bidders

    Args:
        list_of_bidders (list[dict]): Date with name and bid of the bidders

    Returns:
        dict: dict with the name and value of bid made by bidder winner.
    """
    max_bid = 0
    name_of_winner = ''
    for bidder in list_of_bidders:
        if bidder["bid"] > max_bid:
            max_bid = bidder["bid"]
            name_of_winner = bidder['name']

    bidder_winner = {"name": name_of_winner, "bid": max_bid}

    return bidder_winner


while restart:
    print(logo)

    add_bidders(input(ms1).capitalize(), float(input(ms2)))

    if input(msg).lower() == 'yes':
        restart = True
        system('clear')
    else:
        restart = False
        system('clear')

        for person in bidders:
            print(person)
        print('=============')
        winner_dict = winner(bidders)
        print(f'Winner: {winner_dict["name"]} with ${winner_dict["bid"]}')
