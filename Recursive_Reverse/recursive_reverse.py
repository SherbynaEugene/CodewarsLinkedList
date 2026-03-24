'''Reverses a linked list recursively.'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    '''Reverses a linked list recursively.'''
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)

    head.next.next = head
    head.next = None

    return new_head
