'''Splits a linked list into two lists, one with the odd nodes and one with the even nodes.'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''Context class for reference'''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''Splits a linked list into two lists, one with the odd nodes and one with the even nodes.'''
    if head is None or head.next is None:
        raise ValueError
    curNode = head.next # 2
    first = oddNode = head # 1
    second = evenNode = head.next# 2
    count = 2
    while curNode.next is not None:
        count +=1
        curNode = curNode.next # 3
        if not count % 2:
            evenNode.next = curNode
            evenNode = evenNode.next
        else:
            oddNode.next = curNode
            oddNode = oddNode.next
    oddNode.next = None
    evenNode.next = None  
    return Context(first, second)
