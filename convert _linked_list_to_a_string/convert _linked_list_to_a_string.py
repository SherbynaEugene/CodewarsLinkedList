'''Converts a linked list to a string representation.'''

def stringify(node):
    '''Converts a linked list to a string representation.
    >>> stringify(None)
    'None'
    >>> stringify(Node(1))
    '1 -> None'
    >>> stringify(Node(1, Node(2, Node(3))))
    '1 -> 2 -> 3 -> None'
    '''
    curNode = node
    result = ''
    while curNode is not None:
        result += str(curNode.data)
        result += ' -> '
        curNode = curNode.next
    result += 'None'
    return result
