# TODO:
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# APPROACHES:
# ---------------------------------------------------------------
# 1. Check the string first! If the end string is 2 or more than first string OR 2 or more than first string THIS IS FALSE ALREADY as there is more than a change
# 2. Now we are certain string had just one change in terms of length... 
# 3. Check strings from both sides!