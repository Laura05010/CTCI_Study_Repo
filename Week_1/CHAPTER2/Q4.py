# TODO:
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

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
    # More GENERAL initializer??
    # def __init__(self, items: list) -> None:
    #     """Initialize a new linked list containing the given items.

    #     The first node in the linked list contains the first item
    #     in <items>.
    #     """
    #     self._first = None
    #     for item in items:
    #         self.append(item)
    # Transversing Linked Lists
    def print_items(self) -> None:
        """Print out each item of the linked_list"""
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def append(self, item: Any) -> None:
        """Add the given item to the end of this linked list."""
        curr = self._first
        if curr is None:
            # add the new node to the list
            new_node = _Node(item) # Creates new node
            self._first = new_node # Actually assigns to linked list

        else:
            #1. go through the linked list and find last item
            #2. assign reference to last items.next
            while curr.next is not None:
                curr = curr.next
            # Here we know that curr.next is None
            new_node = _Node(item)
            curr.next = new_node

    def partition(self, partition_item: Any) -> None:
        """
        Partition a linked list around a value x, such that all nodes less than x come
        before all nodes greater than or equal to x.
        """
        lower = LinkedList()
        upper = LinkedList()
        curr = self._first
        while curr is not None:
            if curr.item < partition_item:
                lower.append(curr.item)
            else:
                upper.append(curr.item)
            curr = curr.next

        curr_lower = lower._first
        while curr_lower.next is not None:
            curr_lower = curr_lower.next
        curr_lower.next = upper._first
        self = lower