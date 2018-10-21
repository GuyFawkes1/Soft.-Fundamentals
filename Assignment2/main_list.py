from node import *
from LinkedList import *
from list_node import *


class main_list():
    def __init__(self, head=None):
        self.head = list_node(head)

    def insert(new_list_node):
        temp = self.head
        new_list_node.next = self.head
        self.head = new_list_node
