# TODO:
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.


# APPROACHES:
# ---------------------------------------------------------------
# LAURA:
# -> Using a list to store the main permutations of the word to be checked then use the other word to see if its equal to any of the permutations.

from typing import List

def is_permutation(string1:str, string2:str) -> bool:
    # Get the permutations of the string you want to check
    permutations = get_permutations(string2)
    # Check if any of these permutations matches the string
    for permutation in permutations:
        if string1 == permutation:
            return True
    # by this point there are no matching permutations, so:
    return False


def get_permutations(string2:str) -> List:
    pass 


