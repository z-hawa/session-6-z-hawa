import inspect
import os
import re

import pytest

import session_6a
import test_session_6a

full_list_of_cards = [('2', 'spades'), ('3', 'clubs'), ('4', 'hearts'), ('5', 'diamonds'), ('6', 'spades'),
                      ('7', 'clubs'), ('8', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('jack', 'clubs'),
                      ('queen', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('2', 'clubs'), ('3', 'hearts'),
                      ('4', 'diamonds'), ('5', 'spades'), ('6', 'clubs'), ('7', 'hearts'), ('8', 'diamonds'),
                      ('9', 'spades'), ('10', 'clubs'), ('jack', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'),
                      ('ace', 'clubs'), ('2', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('5', 'clubs'),
                      ('6', 'hearts'), ('7', 'diamonds'), ('8', 'spades'), ('9', 'clubs'), ('10', 'hearts'),
                      ('jack', 'diamonds'), ('queen', 'spades'), ('king', 'clubs'), ('ace', 'hearts'),
                      ('2', 'diamonds'), ('3', 'spades'), ('4', 'clubs'), ('5', 'hearts'), ('6', 'diamonds'),
                      ('7', 'spades'), ('8', 'clubs'), ('9', 'hearts'), ('10', 'diamonds'), ('jack', 'spades'),
                      ('queen', 'clubs'), ('king', 'hearts'), ('ace', 'diamonds')]
README_CONTENT_CHECK_FOR = [
    'royal_flush',
    'straight_flush',
    'four_of_a_kind',
    'full_house',
    'flush',
    'straight',
    'three_of_a_kind',
    'two_two_pair',
    'one_two_pair',
    'high_card',
    'lambda',
    'map',
    'zip',
]


def test_readme_exists():
    assert os.path.isfile(
        "README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md",
                  "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10



def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session_6a, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session_6a, inspect.isfunction)
    assert len(functions) > 20, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session_6a, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_function_doc_string():
    """
    Test case to check whether the functions have docstrings or not.
    """
    functions = inspect.getmembers(session_6a, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_deck_lam():
    assert set(session_6a.cards_deck_lambda()) == set(
        full_list_of_cards), 'Incorrect cards using Lambda operation'
    assert len(
        session_6a.cards_deck_lambda) == 52, 'Incorrect number of cards using Lambda operation'

def test_royal_flush():
    hand = [('ace', 'hearts'), ('king', 'hearts'),
            ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    assert session_6a.check_royal_flush(
        hand)[1] == 1, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_straight_flush():
    hand = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'),
            ('jack', 'spades'), ('10', 'spades')]
    assert session_6a.check_straight_flush(
        hand)[1] == 2, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_four_kind():
    hand = [('queen', 'hearts'), ('queen', 'diamonds'),
            ('queen', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert session_6a.check_four_of_a_kind(hand)[1] == 3, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_full_house():
    hand = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'),
            ('king', 'spades'), ('king', 'diamonds')]
    assert session_6a.check_full_house(
        hand)[1] == 4, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_flush():
    hand = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'),
            ('4', 'spades'), ('7', 'spades')]
    assert session_6a.check_flush(hand)[1] == 5, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_straight():
    hand = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'),
            ('jack', 'spades'), ('10', 'hearts')]
    assert session_6a.check_straight(hand)[1] == 6, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_three_kind():
    hand = [('queen', 'hearts'), ('queen', 'spades'),
            ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    assert session_6a.check_three_of_a_kind(hand)[1] == 7, 'Bhai kya kar raha hai , usko hara diya tu ne'
def test_two_pair():
    hand = [('king', 'hearts'), ('king', 'spades'),
            ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert session_6a.check_two_two_pair(hand)[1] == 8, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_one_pair():
    hand = [('king', 'clubs'), ('king', 'spades'),
            ('jack', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert session_6a.check_one_two_pair(hand)[1] == 9, 'Bhai kya kar raha hai , usko hara diya tu ne'

def test_high_card():
    hand = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert session_6a.check_high_card(hand)[1] == 10, 'Bhai kya kar raha hai , usko hara diya tu ne'



def test_deck_cards():
    ALL_CARDS_PRESENT = True
    deck = []
    deck = session_6a.create_deck_function(deck)
    for card in full_list_of_cards:
        if card not in deck:
            ALL_CARDS_PRESENT = False
        else:
            pass
    assert ALL_CARDS_PRESENT == True, "Some cards are missing!"


def test_deck_creation_raises_error():
    deck = 10
    with pytest.raises(TypeError, match=r"*Invalid type provided , must be a list!*"):
        deck = session_6a.create_deck_function(deck)

def test_20_combos():

    # 1
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    p2 = [('queen', 'spades'), ('queen', 'hearts'),
          ('8', 'clubs'), ('5', 'hearts'), ('7', 'hearts')]
    assert "Player 2" in session_6a.determine_winner(p1,p2), "Failed"

    # 2
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),('5', 'spades')]
    p2 = [('2', 'clubs'), ('ace', 'clubs'), ('5', 'clubs')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed"

    # 3
    p1 =[('ace', 'spades'), ('queen', 'diamonds'),('5', 'spades')]
    p2 = [('2', 'clubs'), ('queen', 'clubs'), ('5', 'clubs')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed"

    # 4
    p1 = [('3', 'spades'), ('2', 'hearts'), ('3', 'hearts'),
          ('2', 'diamonds'), ('queen', 'hearts')]
    p2 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed"

    # 5
    p1 = [('jack', 'diamonds'), ('8', 'diamonds'), ('10', 'diamonds')]
    p2 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed"

    # 6
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs')]
    p2 = [('queen', 'clubs'), ('king', 'diamonds'),
          ('queen', 'hearts'), ('9', 'spades')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed"

    # 7
    p1 = [('5', 'spades'), ('6', 'spades'), ('4', 'diamonds'), ('3', 'clubs')]
    p2 =[('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed"

    # 8
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    p2 = [('ace', 'diamonds'), ('queen', 'diamonds'),
          ('queen', 'clubs'), ('queen', 'hearts'), ('4', 'diamonds')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 9
    p1 = [('ace', 'spades'), ('ace', 'diamonds'),
          ('jack', 'spades'), ('ace', 'clubs')]
    p2 = [('king', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 10
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    p2 = [('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'),
          ('jack', 'hearts'), ('7', 'diamonds')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 11
    p1 = [('jack', 'clubs'), ('queen', 'clubs'),
          ('10', 'clubs'), ('king', 'clubs'), ('ace', 'clubs')]
    p2 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 12
    p1 = [('jack', 'clubs'), ('queen', 'clubs'),
          ('10', 'clubs'), ('king', 'clubs'), ('9', 'clubs')]
    p2 =[('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 13
    p1 = [('3', 'hearts'), ('10', 'hearts'),
          ('king', 'hearts'), ('8', 'hearts')]
    p2 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 14
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs')]
    p2 = [('jack', 'hearts'), ('8', 'diamonds'),
          ('jack', 'spades'), ('8', 'clubs')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 15
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs')]
    p2 = [('jack', 'clubs'), ('jack', 'hearts'),
          ('jack', 'spades'), ('3', 'clubs')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 16
    p1 = [('queen', 'hearts'), ('king', 'hearts'),
          ('ace', 'hearts'), ('jack', 'hearts')]
    p2 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 17
    p1 = [('5', 'clubs'), ('6', 'clubs'), ('4', 'clubs')]
    p2 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 18
    p1 = [('6', 'hearts'), ('6', 'spades'), ('6', 'clubs')]
    p2 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 19
    p1 = [('ace', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    p2 = [('5', 'clubs'), ('6', 'clubs'), ('2', 'clubs'),
          ('3', 'clubs'), ('4', 'clubs')]
    assert 'Player 2' in session_6a.determine_winner(
        p1, p2), "Failed."

    # 20
    p1 = [('4', 'diamonds'), ('3', 'diamonds'), ('2', 'diamonds'),
          ('6', 'diamonds'), ('5', 'diamonds')]
    p2 = [('5', 'hearts'), ('9', 'spades'), ('queen', 'clubs'),
          ('2', 'spades'), ('ace', 'hearts')]
    assert 'Player 1' in session_6a.determine_winner(
        p1, p2), "Failed."

