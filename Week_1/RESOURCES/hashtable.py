# HASHTABLE USING CHAINING
# Is good for problems where a flat "area" isn't enough
# Ex: you have 10 apartments  and need to allocate 100 people
INITIAL_CAPACITY = 50

class HashTable:
    def __init__(self):
        # capacity: determine the size of our internal array
        self.capacity = INITIAL_CAPACITY
        # size: number of elements that have been inserted
        self.size = 0
        # Bucket: Internal array, storing each inserted value in a “bucket” based on the provided key.
        self.buckets = [None] * self.capacity

    def hash(self, key):
        # iterator for each character in the key
        hashsum = 0
        # loop through keys for nodes in bucket
        # enumerate() adds counter to the iterable, where the return object is an enumerate object
        for index, char in enumerate(key):
            #Add (index + key length)**(current char code)
            # Hashsum is the overall representation of the key, we add the index to make the Unicode unique (uniformity is crucial in Hashtables)
            hashsum += (index + len(key)) ** ord(char)
            # The ord() function returns an integer representing the Unicode character, the reverse is char().
            # char() converts an Integer to a Character, while ord() does the reverse.
            # The modulus ensures the hashsum is in the range [0, self.capacity - 1].
            hashsum = hashsum % self.capacity
        return hashsum

class Node:
    def __init__(self, key, value):
        # [(Laura, 10) -> (Max, 52) ->] [() ->] [() ->] [(Albert,100) ->(Anoushka, 48)->] [() ->] [(Aleeza,12) ->]
        # where in this node (Laura, 10) "Laura" is the self.key and 10 is the self.value
        # and the self.next is (Max, 52)
        self.key = key
        self.value = value
        self.next = None # the next node

