from LinkedList import *


class List_node():
    def __init__(self, data=LinkedList(), next=None):
        self.data = data
        self.next = next

    def set_next(self, new_next):
        self.next = new_next
