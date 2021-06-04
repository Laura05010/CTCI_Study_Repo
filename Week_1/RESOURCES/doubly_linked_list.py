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
        # Case 2: there is only one element in the list (first == last)
        elif self._first == self._last:
            temp = self._last # store the first and last element
            self._first = None # remove this element (the same as last)
            self._last = None # remove this element (the same as first)
            return temp.item # return this value
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

    def insert_before(self, node, item) -> None:
        """Given a node in the Linked List, we will insert a node before it.
        """
        # Case 1: Empty node
        if node == None:
            print("The given node is empty, so another node can't go before it")
        # Case 2: Node is not empty
        else:
            new_node = _Node(item)
            # case 1: the first node in Linked list is empty
            if node == self._first:
                node.prev = new_node
                new_node.next = node
                self._first = new_node

            # case 2: the node we are on is in the linked list
            else:
                temp = node.prev
                node.prev = new_node
                new_node.next = node
                new_node.prev = temp
                temp.next = new_node

if __name__ == "__main__":
    new_linked = LinkedList()
    new_linked.append(2)
    new_linked.prepend(9)
    new_linked.append(15)
    new_linked.print_items() # 9 -> 2 -> 15
    print("================================")
    print("printed: " + str(new_linked.pop_front())) # 9
    new_linked.print_items()
    print("================================")
    print("printed: " + str(new_linked.pop_back())) # 15
    new_linked.print_items()
    print("================================")
    print("printed: " + str(new_linked.pop_front())) # 2
    new_linked.print_items()
    print("================================")
    print("printed: " + str(new_linked.pop_back()))
    print("================================")
    new_linked.print_items()
    new_linked.append(2)
    new_linked.prepend(9)
    new_linked.append(15)
    new_linked.insert_after(new_linked._last, 7)
    new_linked.print_items() # 9 -> 2 -> 15 -> 7
    print("================================")
    new_linked.insert_before(new_linked._first, 11)
    new_linked.print_items() # 11 -> 9 -> 2 -> 15 -> 7
    print("================================")
    new_linked.insert_after(new_linked._first, 13)
    new_linked.print_items() # 11 -> 13 -> 9 -> 2 -> 15 -> 7
    print("================================")
    new_linked.insert_before(new_linked._last, 4)
    new_linked.print_items() # 11 -> 13 -> 9 -> 2 -> 15 -> 4 -> 7

