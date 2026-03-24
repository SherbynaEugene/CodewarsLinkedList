'''Counts the number of nodes in a loop in a linked list.'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    '''Counts the number of nodes in a loop in a linked list.'''
    slow = node
    fast = node.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    size = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        size += 1
    return size
