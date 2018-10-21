from LinkedList import *


class List_node():
    def __init__(self, data=None, next=None):
        self.data = LinkedList(data)
        self.next = next

    def set_next(self, new_next):
        self.next = new_next
