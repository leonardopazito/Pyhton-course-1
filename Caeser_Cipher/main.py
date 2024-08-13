from art import logo
from os import system
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

N_OF_LETTER_ALPHABET = len(ALPHABET)


def caesar(start_text: str, shift_amount: int, cipher_direction: str) -> str:
    """Shift each letter of text using the Alphabet as reference. The shift can
    be forward (encode) or backward (decode)

    Args:
        start_text (str): Text that will be shifted
        shift_amount (int): Number of displaced letters in the alphabet
        cipher_direction (str): Encode or decode option.
    Returns:
        str: Caesar text
    """

    if shift_amount == 0:
        end_text = start_text
    else:
        end_text = ''
        shift_amount = shift_amount % N_OF_LETTER_ALPHABET
        # Case where shift_amound > N_OF_LETTER_AlPHABET

        for letter in start_text:
            if letter in ALPHABET:
                position_of_letter = ALPHABET.index(letter)

                if cipher_direction.lower() == 'encode':
                    new_position_of_letter = position_of_letter + shift_amount
                    if not new_position_of_letter > N_OF_LETTER_ALPHABET-1:
                        end_text += ALPHABET[new_position_of_letter]
                    else:
                        new_index = new_position_of_letter -\
                            N_OF_LETTER_ALPHABET
                        # Back to the beginning of the ALPHABET

                        end_text += ALPHABET[new_index]

                else:
                    new_position_of_letter = position_of_letter - shift_amount
                    if not new_position_of_letter < 0:
                        end_text += ALPHABET[new_position_of_letter]
                        # Go to the end of the ALPHABET
                    else:
                        end_text += ALPHABET[new_position_of_letter]

            else:
                end_text += letter

    return end_text


restart = True
while restart:
    print(logo)

    is_direction_corret = False
    while not is_direction_corret:
        msg_of_dir = 'Type "encode" to encrypt, type "decode" to decrypt:\n'
        direction = input(msg_of_dir)
        if direction.lower() in ['encode', 'decode']:
            is_direction_corret = True
        else:
            print('Direction invalid!')

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_text = caesar(text, shift, direction)
    print(f'New {direction} text is {caesar_text}')

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'")\
        .lower() == 'yes'
    if restart:
        system('clear')
    else:
        print('Goodbye!')
