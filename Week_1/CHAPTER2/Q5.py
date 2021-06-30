# TODO:
# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

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

def sum_lists(linked_list_1: LinkedList, linked_list_2: LinkedList) -> LinkedList:
    """Returns a linked list representation of the sum of the two linked lists values as a n-digit number, where n is the number of nodes.
    """
    carry_over = 0
    curr_one = linked_list_1._first
    curr_two = linked_list_2._first
    final_result = LinkedList()
    while curr_one is not None or curr_two is not None:
        if carry_over == 1:
            sum_digit = 1
        sum_digit += curr_one.item + curr_two.item
        if sum_digit > 10:
            carry_over = 1
            final_result.append(sum_digit - 10)
        else:
            carry_over = 0
            final_result.append(sum_digit)
        curr_one = curr_one.next
        curr_two = curr_two.next

    final_curr = final_result._first
    while final_curr is not None:
        final_curr = final_curr.next

    if curr_one is not None:
        final_curr.next = curr_one
    elif curr_two is not None:
        final_curr.next = curr_two

    return final_result

# 999 + 999 = 1998. 8 -> 9 -> 9 -> 1
# 9916 + 109 = 10025, 5 -> 2 -> 0 -> 0 -> 1
# 8 + 5 = 13, 3 -> 2 -> 0 -> 1 ->
# 30
# 999 + 9999 = 10998, 8 -> 9 -> 9 -> 0 -> 1