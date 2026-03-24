'''Removes duplicates from a sorted linked list.'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''Removes duplicates from a sorted linked list.'''
    if head is None:
        return head
    curNode = head
    while curNode.next is not None:
        if curNode.data == curNode.next.data:
            curNode.next = curNode.next.next
        else:
            curNode = curNode.next

    return head
