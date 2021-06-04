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

    def insert(self, index: int, item: Any) -> None:
        """Insert a new node containing item at position <index>.

        Precondition: index >= 0.

        Raise IndexError if index > len(self).

        Note: if index == len(self), this method adds the item to the end
        of the linked list, which is the same as LinkedList.append.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200]'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        """
        if index == 0:
            new_node = _Node(item)
            self._first, new_node.next = new_node, self._first
            # Multiple assignment is good for complex state updating
        else:
            curr = self._first
            current_index = 0
            # if we want the node to be inserted into position index,
            # we need to access the node at position (index-1)
            while curr is not None and current_index < index - 1:
                curr = curr.next
                current_index += 1

            # assert curr is None or curr_index == index - 1
            if curr is None:
                # This list doesn't have a node at the given
                # position so index error must be raised
                raise IndexError
            else: # curr_index == index - 1
                # index - 1 is in bounds. Insert the new item.
                new_node = _Node(item)
                new_node.next = curr.next   # Saves the reference and assigns it to the new node
                curr.next = new_node # assigns new node to this node, and next node isnt lost,
                #We assigned it in the previous line!

    def pop(self, index: int) -> Any:
        """Remove and return node at position <index>.

        Precondition: index >= 0.

        Raise IndexError if index >= len(self).

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(2)
        10
        >>> lst.pop(0)
        1
        """
        # Warning: the following is pseudo-code, not valid Python code!

        # 1. If the list is empty, you know for sure that index is out of bounds...
        # 2. Else if index is 0, remove the first node and return its item.
        # 3. Else iterate to the (index-1)-th node and update links to remove
        #    the node at position index. But don't forget to return the item!

        curr = self._first
        current_index = 0

        while curr is not None and current_index < (index - 1) :
            curr = curr.next
            current_index += 1
        if curr is None:    # List is empty: INDEX IS OUT OF BOUNDS!!
            raise IndexError
        else:
            curr.item, curr.next = curr.next.item, curr.next.next
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