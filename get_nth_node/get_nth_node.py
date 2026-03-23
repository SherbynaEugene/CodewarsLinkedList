# from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None or not isinstance(index, int):
        raise ValueError

    count = 0
    curNode = node

    while curNode is not None and count != index:
        count += 1
        curNode = curNode.next

    if curNode is None:
        raise ValueError

    return curNode
