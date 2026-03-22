'''Converts a linked list to a string representation.'''

def stringify(node):
    '''Converts a linked list to a string representation.
    >>> stringify(None)
    'None'
    '''
    curNode = node
    result = ''
    while curNode is not None:
        result += str(curNode.data)
        result += ' -> '
        curNode = curNode.next
    result += 'None'
    return result
