from node import *
from LinkedList import *
from list_node import *


class main_list():
    def __init__(self, head=None):
        self.head = list_node(head)

    def insert(new_list_node):
        temp = self.head
        if temp!=None:
            while temp.next!=None:
                temp=temp.next
            temp.next=list_node(new_list_node.data)
        else:
            self.head=list_node(new_list_node.data)
