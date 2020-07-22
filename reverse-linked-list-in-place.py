class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

#Time Complexity O(n)
#Space O(1)
def reverse_linked_list(head_of_list):
    #each node's next pointer shoud point to the previous node
    current_node = head_of_list
    next_node = None
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node = previous_node
        previous_node = next_node
    return previous_node

#Recursive
#Time Complexity O(n)
#Space O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
