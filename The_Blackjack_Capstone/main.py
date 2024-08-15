import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# ======== To score and to deal card ============
def score(cards_in_hand: list[int]) -> int:
    """Add up the value of all cards in your hand"""
    return sum(cards_in_hand)


def deal_card(deck: list[int], number_of_card: int) -> list[int]:
    """Choose a random card of the deck """
    new_cards = []
    if number_of_card > 0:
        for card in range(0, number_of_card):
            new_cards.append(random.choice(deck))
    return new_cards


# ============ Analyzing the cases ================
def there_is_a_winner_with_21(your_score: int, computer_score: int) -> bool:
    """ Indicates if there is someone with 21"""

    if your_score == 21 and computer_score == 21:
        print('Draw: Both have 21 points.')
        return True

    elif your_score == 21 or computer_score == 21:
        if your_score == 21:
            print("You won.")
        else:
            print('The computer won.')
        return True

    elif (your_score > 21 or computer_score > 21):
        # Cheking if someone lost but has the card 11
        if 11 in your_cards:
            score_test = your_score - 10
            # -10 = -your_cards[your_cards.index(11)] + 1
            if score_test == 21:
                your_cards[your_cards.index(11)] = 1

        if 11 in computer_cards:
            score_computer_test = computer_score - 10
            if score_computer_test == 21:
                computer_cards[computer_cards.index(11)] = 1

        # Cheking again if there is a winner
        if score(your_cards) == 21 or score(computer_cards) == 21:
            if score(your_cards) == 21:
                print('You won')
            else:
                print('The computer Won')
            return True
        return False
    else:
        return False


def is_there_a_loser(your_score: int, computer_score: int) -> bool:
    """Check if anyone is over 21"""

    if not there_is_a_winner_with_21(your_score, computer_score):
        if your_score > 21 or computer_score > 21:
            if your_score == computer_score:
                print("You and the computer lose.")
            elif your_score > 21:
                print('You lose')
            else:
                print('The computer lose')
            return True
    return False


def is_there_a_winner(your_score: int, computer_score: int) -> bool:
    """check who won when both have less than 21 points"""

    if (your_score < 21) and (computer_score < 21):
        if your_score == computer_score:
            print(f'Draw: Both have {your_score} points.')
            return False
        elif your_score < computer_score:
            print("Computer won")
            return True
        else:
            print('You won')
            return True
    else:
        return False


# ==============================================
play = True
while play:
    system('clear')
    # Initial deal of card
    your_cards = deal_card(cards, 2)
    computer_cards = deal_card(cards, 2)

    # Initial score
    your_cards_score = score(your_cards)
    computer_cards_score = score(computer_cards)

    print(f'Your cards: {your_cards}. Score: {your_cards_score}')
    print(f"Computer's first card: {computer_cards[0]}")

    another_card: bool = input("Type 'y' to get another card,\
 type 'n' to pass: ").lower() == 'y'

    while another_card:
        system('clear')
        your_cards.append(*deal_card(cards, 1))
        your_cards_score += your_cards[-1]

        print(f'Your cards: {your_cards}. Score: {your_cards_score}')
        print(f"Computer's first card: {computer_cards[0]}")
        if (there_is_a_winner_with_21(your_cards_score,
                                      computer_cards_score)
                or is_there_a_loser(your_cards_score, computer_cards_score)):
            another_card = False
        else:
            another_card = input("Type 'y' to get another card,\
type 'n' to pass: ").lower() == 'y'

    # Choice of computer
    while score(computer_cards) < 17:
        computer_cards.append(*deal_card(cards, 1))
        computer_cards_score += computer_cards[-1]
    # =============================================

    system('clear')
    print(f'Your cards: {your_cards}. Score: {your_cards_score}')
    print(
        f"The computer's cards: {computer_cards}. Score:\
 {computer_cards_score}")

    print("========")

    if (there_is_a_winner_with_21(your_cards_score, computer_cards_score)
        or is_there_a_loser(your_cards_score, computer_cards_score) or
            is_there_a_winner(your_cards_score, computer_cards_score)):
        play = input("Type 'y' to play again or\
 type 'n' to end: ").lower() == 'y'
