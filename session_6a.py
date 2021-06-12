import random
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
vals_mapped = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 11, 'queen': 12,
               'king': 13, 'ace': 14}
suits = ['spades', 'clubs', 'hearts', 'diamonds']
cards_deck = []


def create_deck_function(deck: list) -> list:
    """Creates a poker deck out of a provided list
    """
    if not isinstance(deck, list):
        raise TypeError("Invalid type provided , must be a list!")
    for i in range(52):
        deck.append(((vals * 4)[i], (suits * 13)[i]))
    return deck


cards_deck = create_deck_function(cards_deck)

cards_deck_lambda = lambda deck: list(map(lambda x: (x[0], x[1]), zip(vals * 4, suits * 13)))


def check_royal_flush(current_hand: list):
    """Checks ifs the provided deck is eligible to win a royal flush"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    all_suits = [y for x, y in current_hand]
    # Since there is only one suit allowed
    if len(set(all_suits)) != 1:
        return False, 11
    royal_flush_numbers = [10, 11, 12, 13, 14]
    all_vals.sort()
    if all_vals == royal_flush_numbers:
        return True, 1
    else:
        return False, 11

def check_straight_flush(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a straight flush"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    all_suits = [y for x, y in current_hand]
    # Since there is only one suit allowed
    if len(set(all_suits)) != 1:
        return False, 11
    all_vals.sort()
    if len(all_vals) != 5:
        return False, 11
    previous_number = all_vals[0]
    return_value = True
    for number in all_vals[1:]:
        if previous_number + 1 != number:
            return_value = False
        previous_number = number
    if return_value:
        return True, 2
    previous_number = all_vals[4]
    for number in all_vals[4::-1]:
        if previous_number - 1 != number:
            return False, 11
        previous_number = number
    else:
        return True, 2


def check_four_of_a_kind(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a four of a kind"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    # DO NOT NEED SUITS HERE SO all_suits = [y for x, y in current_hand]
    only_values = list(set(all_vals))
    if len(all_vals) < 4:
        return False, 11
    for number in only_values:
        if all_vals.count(number) == 4:
            return True, 3
    else:
        return False, 11


def check_full_house(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a full house"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    if len(all_vals) != 5:
        return False, 11
    all_vals.sort()
    ace_count = 0
    king_count = 0
    for card in all_vals:
        if card == 14:
            ace_count += 1
        elif card == 13:
            king_count += 1
    if ace_count == 3 and king_count == 2:
        return True, 4
    else:
        return False, 11


def check_flush(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a flush"""
    all_suits = [y for x, y in current_hand]
    if len(set(all_suits)) == 1:
        return True, 5
    else:
        return False, 11


def check_straight(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a straight"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    all_vals.sort()
    previous_number = all_vals[0]
    return_value = True
    for number in all_vals[1:]:
        if previous_number + 1 != number:
            return_value = False
        previous_number = number
    if return_value:
        return True, 6
    previous_number = all_vals[-1]
    for number in all_vals[-1::-1]:
        if previous_number - 1 != number:
            return False, 11
        previous_number = number
    else:
        return True, 6


def check_three_of_a_kind(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a three of a kind"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    all_vals.sort()
    only_values = list(set(all_vals))
    for number in all_vals:
        if all_vals.count(number) == 3:
            return True, 7
    else:
        return False, 11


def check_two_two_pair(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a two pair"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    all_vals.sort()
    only_values = list(set(all_vals))
    count = 0
    for number in only_values:
        if all_vals.count(number) == 2:
            count += 1
    if count >= 2:
        return True, 8
    else:
        return False, 11


def check_one_two_pair(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a one pair"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    all_vals.sort()
    if len(all_vals) < 4:
        return False, 11
    if len(set(all_vals)) == len(all_vals) - 1:
        return True, 9
    else:
        return False, 11


def check_high_card(current_hand: list) -> tuple:
    """Checks ifs the provided deck is eligible to win a high card"""
    all_vals = [vals_mapped[x] for x, y in current_hand]
    if 14 in all_vals:
        return True, 10
    else:
        return False, 11


def determine_winner(player1_hand: list, player2_hand: list) -> str:
    """Tasty spaghetti which checks who won the game provided two card decks"""
    player1_won, player1_number = check_royal_flush(player1_hand)
    if not player1_won:
        player1_won, player1_number = check_straight_flush(player1_hand)
        if not player1_won:
            player1_won, player1_number = check_four_of_a_kind(player1_hand)
            if not player1_won:
                player1_won, player1_number = check_full_house(player1_hand)
                if not player1_won:
                    player1_won, player1_number = check_flush(player1_hand)
                    if not player1_won:
                        player1_won, player1_number = check_straight(player1_hand)
                        if not player1_won:
                            player1_won, player1_number = check_three_of_a_kind(player1_hand)
                            if not player1_won:
                                player1_won, player1_number = check_two_two_pair(player1_hand)
                                if not player1_won:
                                    player1_won, player1_number = check_one_two_pair(player1_hand)
                                    if not player1_won:
                                        player1_won, player1_number = check_high_card(player1_hand)
    player2_won, player2_number = check_royal_flush(player2_hand)
    if not player2_won:
        player2_won, player2_number = check_straight_flush(player2_hand)
        if not player2_won:
            player2_won, player2_number = check_four_of_a_kind(player2_hand)
            if not player2_won:
                player2_won, player2_number = check_full_house(player2_hand)
                if not player2_won:
                    player2_won, player2_number = check_flush(player2_hand)
                    if not player2_won:
                        player2_won, player2_number = check_straight(player2_hand)
                        if not player2_won:
                            player2_won, player2_number = check_three_of_a_kind(player2_hand)
                            if not player2_won:
                                player2_won, player2_number = check_two_two_pair(player2_hand)
                                if not player2_won:
                                    player2_won, player2_number = check_one_two_pair(player2_hand)
                                    if not player2_won:
                                        player2_won, player2_number = check_high_card(player2_hand)
    if player1_number < player2_number:
        return "Player 1"
    elif player2_number < player1_number:
        return "Player 2"
    else:
        return "It's a draw"
