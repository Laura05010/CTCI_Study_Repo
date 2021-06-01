# TODO:
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #7 7 7, #732
# 1 + 1 = 2?

# APPROACHES:
# ---------------------------------------------------------------
# LAURA:
# -> Counter create a counter using a hash map/dictionary that maps alphabet to number of letters per word
# -> If value (number) > 1 then return false because the aren’t unique letters in the word

def has_unique_chars(string: str) -> bool:
    """Determines if a string has all unique characters
    >>> has_unique_chars("Laura")
    False
    >>> has_unique_chars("Chris")
    True
    >>> has_unique_chars("This has to be false")
    False
    """
    word_chars = dict()
    for char in string:
        if char in word_chars:
            word_chars[char] += 1
            # Only once we know that there is at least a chance that the char is in the dictionary then we can be sure whether it's unique or not.
            if word_chars[char] > 1:
                return False
        else:
            word_chars[char] = 1
    # We got through the string and had no issues all have been unique so far
    return True

if __name__ == '__main__':
    print(has_unique_chars("Laura"))
    print(has_unique_chars("Chris"))
    print(has_unique_chars("This has to be false"))
    print(has_unique_chars("Hello"))