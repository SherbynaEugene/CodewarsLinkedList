'''Swaps pairs of nodes in a linked list.'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    '''Swaps pairs of nodes in a linked list.'''
    if head is None or head.next is None:
        return head
    real_head = head.next
    pastNode = None
    prevNode = head
    curNode = head.next
    while 1:
        prevNode.next = curNode.next # A -> C
        curNode.next = prevNode # B -> A
        if pastNode is not None:
            pastNode.next = curNode
        pastNode = prevNode
        if pastNode.next is not None and pastNode.next.next is not None:
            prevNode = pastNode.next
            curNode = pastNode.next.next
        else:
            break
    return real_head
