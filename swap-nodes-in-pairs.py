# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# First, we swap the first two nodes in the list, i.e. head and head.next;
# Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
# Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    first = head
    second = head.next

    first.next = swapPairs(second.next)
    second.next = first

    return second
