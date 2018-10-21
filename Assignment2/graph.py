from list_node import *
from node import *
from LinkedList import *
from main_list import *


class graph():
    def __init__(self):
        self.adj = main_list()

    def add_edge(self, node_a, node_b):
        search1 = 0
        search2 = 0
        temp = self.adj.head
        if(temp == None):
            p = LinkedList(node(a.team1, a.team2))
            p.insert(node(b.team1, b.team2))
            self.adj.insert(List_node(p))

            if(a.compare(b) == 1):
                return
            else:
                q = LinkedList(node(b.team1, b.team2))
                q.insert(node(a.team1, a.team2))

                self.adj.insert(List_node(q))
                # // this.print_graph();
                # // System.out.println("Ohbgvfcd");
                return

        while(temp.next != None):
                # // System.out.print("d1");
            if(temp.data.head.compare(a) == 1):
                temp.data.insert(b)
                search1 = 1
            if(temp.data.head.compare(b) == 1):
                temp.data.insert(a)
                search2 = 1
            temp = temp.next

        if(search1 == 0):
            if(temp.data.head.compare(a) == 1):
                temp.data.insert(b)
            else:
                p = LinkedList(a)
                p.insert(b)
                self.adj.insert(List_node(p))

        if(search2 == 0):
            if(temp.data.head.compare(b) == 1):
                temp.data.insert(a)
            else:
                q = LinkedList(b)
                q.insert(a)
                self.adj.insert(list_node(q))

    def print_graph():
        temp = adj.head
        while(temp != null):
            print("("+temp.data.head.team1+","+temp.data.head.team2+"),")
            temp2 = temp.data.head.next
            while(temp2 != null):
                print("("+temp2.team1+","+temp2.team2+")")
                temp2 = temp2.next

            print()
            temp = temp.next
