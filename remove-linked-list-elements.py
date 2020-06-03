# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
# Output: 1 -> 2 -> 3 -> 4 -> 5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Intuition

# The problem seems to be very easy if one has to delete a node in the middle:
# Pick the node-predecessor prev of the node to delete.
# Set its next pointer to point to the node next to the one to delete.

# The things are more complicated when the node or nodes to delete are in the head of linked list.


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head 
        prev, curr = sentinel, head 
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next 
        return sentinel.next
