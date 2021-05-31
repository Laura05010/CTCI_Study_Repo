# TODO:
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #7 7 7, #732
# 1 + 1 = 2?
def foo():
    return 1 + 1 == 2

print(foo())

# APPROACHES:
# ---------------------------------------------------------------
# LAURA:
# -> Counter create a counter using a hash map that maps alphabet to number of letters per word
# -> If value (number) > 1 then return false because the aren’t unique letters in the word
