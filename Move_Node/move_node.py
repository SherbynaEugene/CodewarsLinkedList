'''Moves the node from the front of the source list to the front of the destination list.'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''Context class for reference'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''Moves the node from the front of the source list to the front of the destination list.'''
    new_source = source.next
    source.next = dest
    new_dest = source
    return Context(new_source, new_dest)
