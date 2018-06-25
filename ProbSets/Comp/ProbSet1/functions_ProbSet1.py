# functions_ProbSet1.py

from itertools import combinations, permutations

# Function for Problem 1

# The function failed because the square roots of 4, 6, and 8 are between
# 2 and 3, and the int() function throws out the decimals so that the for loop
# doesn't execute. We can fix these base cases by adding 1 to the range of
# the for loop.

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
    # Corrected function by increasing the range of the for loop by 1
    for i in range(2, int(n**.5) + 1):
        if n % i == 0: return i
    return n

# Function for Problem 2
def month_length(month, leap_year=False):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July",
                        "August", "October", "December"}:
        return 31
    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None

# Function for Problem 3
def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")

# Class and Functions for Problem 4
class Fraction(object):
    """Reduced fraction class with integer numerator and denominator."""
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        elif type(numerator) is not int or type(denominator) is not int:
            raise TypeError("numerator and denominator must be integers")

        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
            return a

        common_factor = gcd(numerator, denominator)
        self.numer = numerator // common_factor
        self.denom = denominator // common_factor

    def __str__(self):
        if self.denom != 1:
            return "{}/{}".format(self.numer, self.denom)
        else:
            return str(self.numer)

    def __float__(self):
        return self.numer / self.denom

    def __eq__(self, other):
        if type(other) is Fraction:
            return self.numer==other.numer and self.denom==other.denom
        else:
            return float(self) == other

    # Corrected error in the __add__() method
    def __add__(self, other):
        return Fraction(self.numer*other.denom + self.denom*other.numer,
                            self.denom*other.denom)

    # Corrected error in the __sub__() method
    def __sub__(self, other):
        return Fraction(self.numer*other.denom - self.denom*other.numer,
                            self.denom*other.denom)

    def __mul__(self, other):
        return Fraction(self.numer*other.numer, self.denom*other.denom)

    def __truediv__(self, other):
        if self.denom*other.numer == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return Fraction(self.numer*other.denom, self.denom*other.numer)

# Function for Problems 5 and 6
def count_sets(cards):
    """Return the number of sets in the provided Set hand.

    Parameters:
        cards (list(str)) a list of twelve cards as 4-bit integers in
        base 3 as strings, such as ["1022", "1122", ..., "1020"].

    Returns:
        (int) The number of sets in the hand.

    Raises:
        ValueError: if the list does not contain a valid Set hand, meaning
            - there are not exactly 12 cards,
            - the cards are not all unique,
            - one or more cards does not have exactly 4 digits, or
            - one or more cards has a character other than 0, 1, or 2."""

    # Check for invalid input
    if len(cards) != 12:
        raise ValueError("There are not exactly 12 cards.")
    if len(cards) > len(set(cards)):
        raise ValueError("The cards are not all unique")
    for card in cards:
        if len(card) != 4:
            raise ValueError("One or more cards does have exactly 4 digits")
    for card in cards:
        for num in card:
            if num not in "012":
                raise ValueError("One or more cards has a character other than 0, 1, or 2")

    # Count the number of sets in this hand
    numSets = 0
    combs = list(combinations(cards, 3))
    for potSet in combs:
        if is_set(str(potSet[0]), str(potSet[1]), str(potSet[2])):
            numSets += 1

    return numSets


def is_set(a, b, c):
    """Determine if the cards a, b, and c constitute a set.

    Parameters:
        a, b, c (str): string representations of 4-bit integers in base 3.
            For example, "1022", "1122", and "1020" (which is not a set).
    Returns:
        True if a, b, and c form a set, meaning the ith digit of a, b,
            and c are either the same or all different for i=1,2,3,4.
        False if a, b, and c do not form a set."""

    digit1, digit2, digit3, digit4 = True, True, True, True

    # Make a set of the corresponding digits.
    # If the set of each digit has length 1 or 3, then
    # the cards form a sets.
    digit1Set = {a[0], b[0], c[0]}
    digit2Set = {a[1], b[1], c[1]}
    digit3Set = {a[2], b[2], c[2]}
    digit4Set = {a[3], b[3], c[3]}

    goodLengths = [1, 3]

    if len(digit1Set) not in goodLengths:
        digit1 = False
    if len(digit2Set) not in goodLengths:
        digit2 = False
    if len(digit3Set) not in goodLengths:
        digit3 = False
    if len(digit4Set) not in goodLengths:
        digit4 = False

    return (digit1 and digit2 and digit3 and digit4)
