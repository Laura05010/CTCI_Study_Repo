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
