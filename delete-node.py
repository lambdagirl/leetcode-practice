class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

#modify the current node instead of deleting it
def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next
    
a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
print(a.next.value)
