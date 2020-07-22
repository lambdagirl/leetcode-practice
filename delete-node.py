class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

#modify the current node instead of deleting it
def delete_node(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        raise Exception("Can't delete the last node!")

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
print(a.next.value)

#side effect
#1.First, it doesn't work for deleting the last node in the list.
#2.Any references to the input node have now effectively been reassigned to its next node.
#3.If there are pointers to the input node's original next node, those pointers now point to a "dangling" node
