# TODO: 
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.) 

# APPROACHES:
# ---------------------------------------------------------------
# AS A GROUP:
# 1. Check if string is odd or even
# 2. Hashmap of (letter: number)
# 3. If the word has even number of characters : all letters need to have an even number of (number)
# 4. If the word has odd number of characters: all letters except one (That one letter has an odd number) have an even number of (number)