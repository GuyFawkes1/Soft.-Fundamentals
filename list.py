class list(object):

    def __init__(self,head=None):
        self.head = head

    def insert(self,data):
        temp = self.head
        if temp!= None:
            while(temp.next!=None):
                temp = temp.next
            temp.next = cell(data=data)
        else:
            head = cell(data=data)
    
    def delete(self,data):
        temp   = self.head
        

     

class cell(object):
    
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

