# HASHTABLE USING CHAINING
# Is good for problems where a flat "area" isn't enough
# Ex: you have 10 apartments  and need to allocate 100 people
INITIAL_CAPACITY = 5

class HashTable:
    def __init__(self):
        # capacity: determine the size of our internal array
        self.capacity = INITIAL_CAPACITY
        # size: number of elements that have been inserted
        self.size = 0
        # Bucket: Internal array, storing each inserted value in a “bucket” based on the provided key.
        self.buckets = [None] * self.capacity


    #HASH
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


    #INSERT:
    def insert(self, key, value):
        # 1. Increment size of hash table.
        self.size += 1
        # 2. Compute index of key using hash function.
        index = self.hash(key)
        # Go to node corresponding to hash
        node = self.buckets[index]
        new_node = Node(key,value)
        # 3. If the bucket at index is empty, create a new node and add it there.
        if node is None:
            self.buckets[index] = new_node
            return
        # 4. Otherwise, a collision occurred: there is already a linked list of at least one node at this index. Iterate to the end of the list and add a new node there.

        curr_node = node
        while curr_node.next is not None:
            curr_node = curr_node.next ## -> to reach till end of linked list
        ## Assign at the end
        curr_node.next = new_node

    #FIND
    def find(self, key):
        # 1. Compute the index for the provided key using the hash function.
        index = self.hash(key)
        # 2. Go to the bucket for that index. Aka the first node in the list
        node = self.buckets[index]
        # 3. Traverse through the linked list until the key is found or the end of the list is reached
        while node is not None and node.key != key:
            node = node.next
        # 4. Return the value of the found node or None
        if node is None:
             return None # not found
        return node.value # found

    #REMOVE
    def remove(self, key):
        # 1. Compute hash for the key to determine index.
        index = self.hash(key)
        node = self.buckets[index]
        curr = None

        # 2. Iterate linked list of nodes. Continue until end of list or until key is found.
        while node is not None and node.key != key:
            curr = node
            node = node.next
        # Now, node is either the requested node or none

        if node is None:
            # 3. Key not found, return None
            return None
        # 4. The key was found, remove the node from the linked list and return the node value
        self.size -= -1
        result = node.value
        # Delete this element in linked list
        if curr is None:
            node = None
        else:
            curr.next = curr.next.next

        # Return the deleted language
        return result



class Node:
    def __init__(self, key, value):
        # [(Laura, 10) -> (Max, 52) ->] [() ->] [() ->] [(Albert,100) ->(Anoushka, 48)->] [() ->] [(Aleeza,12) ->]
        # where in this node (Laura, 10) "Laura" is the self.key and 10 is the self.value
        # and the self.next is (Max, 52)
        self.key = key
        self.value = value
        self.next = None # the next node

if __name__ == '__main__':
    HashTable()
    print(hash("john"))
    print(hash("mary"))
    print(hash("george"))