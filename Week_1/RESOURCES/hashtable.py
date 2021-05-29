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

class Node:
    def __init__(self, key, value):
        # [(Laura, 10) -> (Max, 52) ->] [() ->] [() ->] [(Albert,100) ->(Anoushka, 48)->] [() ->] [(Aleeza,12) ->]
        # where in this node (Laura, 10) "Laura" is the self.key and 10 is the self.value
        # and the self.next is (Max, 52)
        self.key = key
        self.value = value
        self.next = None # the next node