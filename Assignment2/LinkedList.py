from node import *


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_element):
        temp= self.head
        if self.head:
            while temp.next:
                if temp.compare(new_element)==1:
                    return
                temp=temp.next
            temp.next=new_element
            if temp.compare(new_element)==1:
                return
            temp.next=node(new_element.team1,new_element.team2)
        else:
            self.head=new_element
    def search(self, element):
        current = self.head
        while current:
            if current.compare(element)==1:
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
