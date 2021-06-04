from __future__ import annotations
from typing import Optional, Any, List
# We use a preceding underscore for the class name to indicate
# that this entire class is private:
# it shouldn’t be accessed by client code directly,
# but instead is only used by the “main” class described in the next section.

# --------------------------- WHY DOUBLY LINKED LISTS? --------------------------------------
# What if you needed a FASTER method to remove the last node in the linked list
# 10 -> 20 -> 30 -> 40
# Becomes
# 10 -> 20 -> 30

# In the normal first linked list we implemented, this is O(n) as we have to traverse it
# to n-1 node to set this node.next to None

# Now... we still need to find the Second last node

# COOL FIX: have a _previous ATTRIBUTE
# DOUBLY LINKED LISTS!!! WOOOT WOOT!!!!!
# --------------------------------------------------------------------------------------------

class _Node:
    """A node in a doubly linked list.
    Note that this is considered a "private class", one which is only meant
    to be used in this module by the DoublyLinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    previous:
        The previous node in the list, or None if there is only one node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    #next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item  # Basically each node hold the item and a reference to the next item!!!
        self.next = None  # Initially pointing to nothing
        self.prev = None  # Initially pointing to nothing

class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]
    _last: Optional[_Node]

    def __init__(self) -> None:
        """Initialize an empty linked list.
        """
        self._first = None
        self._last = None

    def print_items(self) -> None:
        """Print out each item of the linked_list"""
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def to_list(self) -> list:
        """Return a (built-in) list that contains the same elements as this list.
        """
        lst_version = []
        curr = self._first
        while curr is not None: # as long as we havent reached the end of the list
            lst_version.append(curr.item)
            curr = curr.next
        return lst_version

    def __eq__(self, other: LinkedList) -> bool:
        """Return whether this list and the other list are equal.
        Two lists are equal when each one has the same number of items,
        and each corresponding pair of items are equal (using == to compare).
        """
        curr1 = self._first
        curr2 = other._first
        # THE WHILE LOO CONDITION SHOULD
        # ALWAYS BE THE NEGATION OF THE STOPPING CONDITION
        # while not(curr1 is None or curr2 is None)
        # USE DE MORGAN'S LAW
        while curr1 is not None and curr2 is not None:
            if curr1.item != curr2.item:    # checks if items are the same
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        return curr1 is None and curr2 is None  # if thelinked lists are the same!

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.
        Raise an IndexError if the <index> is out of bounds.
        Precondition: index >= 0.
        """
        curr = self._first
        where = 0
        while curr is not None and where < index:
            curr = curr.next
            where += 1
        if curr is not None: # where = index, so just return item
            return curr.item
        raise IndexError # we reached end of LinkedList and index is out of bounds!!!

    # Mutating Linked Lists
    def prepend(self, item: Any) -> None:
        """ Insert item at beginning of self. In other words its our push_front"""
        new_node = _Node(item)
        new_node.next = self._first
        # self._first = new_node    # cant do it here other wise you lose the entire list!!!
        if self._first != None: #if the linked list is not empty
            self._first.prev = new_node # the old _first is the new_node's .prev
            self._first = new_node # change the self._first pointer to the new_node
        else:
            self._first = new_node
            self._last = new_node
        new_node.prev = None

    # RUN TIME APPEND: SLOWWW O(n)
    def append(self, item: Any) -> None:
        """Add the given item to the end of this linked list. This is our push_back"""
        new_node = _Node(item)
        new_node.prev = self._last
        if self._last == None:
            self._last = new_node
            self._first = new_node
            new_node.next = None
        else:
             self._last.next = new_node
             new_node.next = None
             self._last = new_node

    def pop_front(self):
        """Removes and returns the first element
        """
        if self._first == None:
            print("List is empty")

        else:
            temp = self._first # make a temp variable to preserve current first element
            temp.next.prev = None # make the second element the new head
            self._first = temp.next # make the new element the first
            return temp.item # return the value of the removed element

    def pop_back(self):
        """Removes and returns the last element.
        """
        # Case 1: there are no elements in the list (front and last are None)
        if self._last == None:
            print("List is empty")

        # Case 2: there is only one element in the list (first == last)
        elif self._first == self._last:
            temp = self._last # store the first and last element
            self._first = None # remove this element (the same as last)
            self._last = None # remove this element (the same as first)
            return temp.item # return this value

        # Case 3: a regular DLL with more than one element
        else:
            temp = self._last # make a temp variable to preserve last element
            temp.prev.next = None # remove the second element (changes the pointer)
            self._last = temp.prev # reassign the last node
            return temp.item # return the value of the removed element

    def insert_after(self, node, item) -> None:
        """Given a node in the Linked List, we will insert a node after it.
        """
        # Case 1: Empty node
        if node == None:
            print("The given node is empty, so another node can't go after it")
        # Case 2: Node is not empty
        else:
            # case 1: the last node in Linked list is empty
            new_node = _Node(item)
            if node == self._last:
                node.next = new_node # The current node we are on needs to point to new node
                new_node.prev = node # The next node needs to point to current node as its preveious
                self._last = new_node # Reassign self.last

            # case 2: the node we are on is in the linked
            else:
                temp = node.next # Let's put the original next node somewhere for now..
                node.next = new_node # curent node needs to point to new node
                new_node.prev = node # new node has to point back to current node
                # Now we can connect temp node back!
                new_node.next = temp # new node need to point to the temp node
                temp.prev = new_node # the temp node need to point back to the new node



    # FROM THE LAB:
    def __len__(self) -> int:
            """Return the number of elements in this list.

            >>> lst = LinkedList([])
            >>> len(lst)              # Equivalent to lst.__len__()
            0
            >>> lst = LinkedList([1, 2, 3])
            >>> len(lst)
            3
            """
            length = 0
            curr = self._first
            while curr is not None:
                length += 1
                curr = curr.next
            return length

    def count(self, item: Any) -> int:
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.count(1)
        3
        >>> lst.count(2)
        2
        >>> lst.count(3)
        1
        """
        n_item = 0
        curr = self._first
        while curr is not None:
            if curr.item == item:
                n_item += 1
            curr = curr.next
        return n_item

    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of <item> in this list.

        Raise ValueError if the <item> is not present.

        Use == to compare items.

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.index(1)
        0
        >>> lst.index(3)
        3
        >>> lst.index(148)
        Traceback (most recent call last):
        ValueError
        """
        curr_i = 0
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return curr_i
            curr_i += 1
            curr = curr.next
        # we finished and nothing returned so raise Value error
        raise ValueError

    def __setitem__(self, index: int, item: Any) -> None:
        """Store item at position <index> in this list.

        Raise IndexError if index >= len(self).

        >>> lst = LinkedList([1, 2, 3])
        >>> lst[0] = 100  # Equivalent to lst.__setitem__(0, 100)
        >>> lst[1] = 200
        >>> lst[2] = 300
        >>> str(lst)
        '[100 -> 200 -> 300]'
        """
        if index >= len(self):
            raise IndexError
        else:
            curr = self._first
            index_val = 0
            while curr is not None:
                if index_val == index:
                    curr.item = item
                index_val += 1
                curr = curr.next
    #THE QUIZ CODE
    def insert_after(self , marker : Any , item : Any) -> None :
        """ Insert <item> after the first time <marker > occurs in this linked list .
        Precondition : <marker > is in this linked list .
        >>> lst = LinkedList([1 , 3 , 2 , 6])
        >>> lst.insert_after(3 , 4)
        >>> str(lst)
        '[1 -> 3 -> 4 -> 2 -> 6]'
        """
        curr = self._first
        while curr.item != marker :
            curr = curr.next
        insert = _Node(item)
        # curr.next = insert
        # problem: we lose the reference to the rest of the items
        # fix:
        #curr.next, insert.next = insert, curr.next
        # BASICALLY MULTIPLE ASSIGNMENT IS YOUR BFF!
        # The other way...
        insert.next = curr.next
        curr.next = insert

if __name__ == "__main__":
    pass