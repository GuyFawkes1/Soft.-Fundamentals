from node import *


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def search(self, element):
        current = temp.head
        while current:
            if current is element:
                return True
            current = current.next
        return False

    def delete(self, element):
        previous = None
        current = self.head
        if current is element:
            self.head = self.head.next
            return current
        while current.next != element:
            previous = current
            current = current.next
        previous.next = current.next
        return current
