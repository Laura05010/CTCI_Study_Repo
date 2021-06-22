# TODO:
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from __future__ import annotations
from typing import Optional, Any, List
# We use a preceding underscore for the class name to indicate
# that this entire class is private:
# it shouldn’t be accessed by client code directly,
# but instead is only used by the “main” class described in the next section.
class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
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

class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    def __init__(self) -> None:
        """Initialize an empty linked list.
        """
        self._first = None

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

# TODO:
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

def kth_to_last(self, k: int) -> int: # k = 0
    counter = len(self) - k - 1 # 0

    curr = self._first # 1
    while curr is not None:
        if counter == 0:
            return curr.item
        else:
            curr = curr.next # 5
            counter -= 1
    return "K is out of bound"


# HELPER
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

if __name__ == "__main__":
    pass