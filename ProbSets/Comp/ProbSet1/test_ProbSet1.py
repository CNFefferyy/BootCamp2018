# test_ProbSet1.py

import pytest
import functions_ProbSet1 as funcs
from itertools import combinations, permutations

# Tests for Problem 1
def test_smallest_factor():
    assert funcs.smallest_factor(1) == 1
    assert funcs.smallest_factor(4) == 2
    assert funcs.smallest_factor(6) == 2
    assert funcs.smallest_factor(8) == 2
    assert funcs.smallest_factor(16) == 2
    assert funcs.smallest_factor(17) == 17

# Tests for Problem 2
def test_month_length():
    assert funcs.month_length("September") == 30
    assert funcs.month_length("January") == 31
    assert funcs.month_length("February") == 28
    assert funcs.month_length("February", leap_year=True) == 29
    assert funcs.month_length("Rebekah") == None

# Tests for Problem 3
def test_operate():
    with pytest.raises(TypeError) as excinfo:
        funcs.operate(0, 0, 0)
    assert funcs.operate(4, 1, '+') == 5
    assert funcs.operate(4, 1, '-') == 3
    assert funcs.operate(5, 0, '*') == 0
    with pytest.raises(ZeroDivisionError) as excinfo:
        funcs.operate(5, 0, '/')
    assert funcs.operate(5, 1, '/') == 5
    with pytest.raises(ValueError) as excinfo:
        funcs.operate(5, 1, 'a')

# Tests for Problem 4
@pytest.fixture
def set_up_fractions():
    frac_1_3 = funcs.Fraction(1, 3)
    frac_1_2 = funcs.Fraction(1, 2)
    frac_n2_3 = funcs.Fraction(-2, 3)
    frac_1_1 = funcs.Fraction(1, 1)
    frac_0_1 = funcs.Fraction(0, 1)
    return frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1

def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = funcs.Fraction(30, 42) # 30/42 reduces to 5/7.
    assert frac.numer == 5
    assert frac.denom == 7

    with pytest.raises(ZeroDivisionError) as excinfo:
        funcs.Fraction.__init__('Test', 3, 0)
    with pytest.raises(TypeError) as excinfo:
        funcs.Fraction.__init__('Test', 3.5, 2)

def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert str(frac_1_3) == "1/3"
    assert str(frac_1_2) == "1/2"
    assert str(frac_n2_3) == "-2/3"
    assert str(frac_1_1) == "1"

def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert frac_1_2 == funcs.Fraction(1, 2)
    assert frac_1_3 == funcs.Fraction(2, 6)
    assert frac_n2_3 == funcs.Fraction(8, -12)

    assert float(frac_n2_3) == frac_n2_3

def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert frac_1_2 + frac_1_3 == funcs.Fraction(5, 6)

def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert frac_1_2 - frac_1_3 == funcs.Fraction(1, 6)

def test_fraction_mul(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert frac_1_2 * frac_1_3 == funcs.Fraction(1, 6)

def test_fraction_div(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_fractions
    assert frac_1_2 / frac_1_3 == funcs.Fraction(3, 2)
    with pytest.raises(ZeroDivisionError) as excinfo:
        frac_1_2 / frac_0_1

# Test for the Set game, Problem 5 and 6
@pytest.fixture
def set_up_hands():
    hand1 = ["1022", "1122", "0100", "2021", "0010", "2201",
             "2111", "0020", "1102", "0210", "2110", "1020"]
    handWrongNumCards = ["0000"]
    handNotUnique = ["0000", "0000", "0000", "0000", "0000", "0000",
                     "0000", "0000", "0000", "0000", "0000", "0000"]
    handWrongDigits = ["00000", "1122", "0100", "2021", "0010", "2201",
                       "2111", "0020", "1102", "0210", "2110", "1020"]
    handWrongChar = ["3022", "1122", "0100", "2021", "0010", "2201",
                     "2111", "0020", "1102", "0210", "2110", "1020"]
    return hand1, handWrongNumCards, handNotUnique, handWrongDigits, handWrongChar

def test_count_sets():
    hand1, handWrongNumCards, handNotUnique, handWrongDigits, handWrongChar = set_up_hands()
    assert funcs.count_sets(hand1) == 6
    # Raises ValueError if there are not exactly 12 cards
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handWrongNumCards)
    # Raises ValueError if the cards are not all unique
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handNotUnique)
    # Raises ValueError if one or more cards does not have exactly 4 digits
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handWrongDigits)
    # Raises ValueError if one or more cards has a character other than 0, 1, 2
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handWrongChar)

def test_is_set():
    # Different in all aspects
    assert funcs.is_set("0000", "1111", "2222") == True
    assert funcs.is_set("1022", "1122", "1020") == False
    assert funcs.is_set("1020", "1120", "1220") == True
