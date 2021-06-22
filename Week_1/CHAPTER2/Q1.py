# TODO:
# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

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

# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
    def remove_dups(self):
        """remove duplicates from an unsorted linked list.
        """
        buffer = []
        curr = self._first
        while curr.next is not None:
            if curr.next.item in buffer:
                # Skip over the value
                curr.next = curr.next.next
            else:
                buffer.append(curr.item)
            curr = curr.next

# SOLUTION WITHOUT THE BUFFER
    def remove_dups2(self):
        """remove duplicates from an unsorted linked list without a buffer.
        """
        curr = self._first
        while curr is not None:
            # Assigning a runner to keep track of duplicates
            runner = curr
            while runner.next is not None:
                if runner.next.item == curr.item :
                    # Remove this duplicate
                    runner.next = runner.next.next
                # We haven't found a duplicate so just continue
                else:
                    runner = runner.next
            curr = curr.next


if __name__ == "__main__":
    pass