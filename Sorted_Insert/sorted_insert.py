'''Inserts a node into a sorted linked list.'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    '''Inserts a node into a sorted linked list.'''
    curNode = head
    prevNode = None
    newNode = Node(data)
    while curNode is not None and curNode.data <= data:
        prevNode = curNode
        curNode = curNode.next
    if prevNode:
        prevNode.next = newNode
    else:
        head = newNode
    newNode.next = curNode

    return head
