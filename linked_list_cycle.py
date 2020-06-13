
# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position(0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


# Example 1:

# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1, 2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

class Solution1:
    def hasCycle(self, head: ListNode) -> bool:

        visit_dic = {}
        while head:
            if head in visit_dic:
                return True
            else:
                visit_dic[head] = 0
            head = head.next
        return False


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:

        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
