'''Parses a string representation of a linked list and constructs the linked list.'''

from xml.dom.minidom import Node
# from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    '''Parses a string representation of a linked list and constructs the linked list.'''
    datas = list_repr.split(' -> ')
    datas.remove('None')
    result = None
    for data in reversed(datas):
        result = Node(int(data), result)
    return result
