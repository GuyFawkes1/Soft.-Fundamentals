class Mfset:
    
    def __init__(self,vertices):
        self.setarray =  [0 for i in range(1,vertices+1)]
        self.nosets = 0
    
    def find(self,x):
        return self.setarray[x]

    def insertnew(self,v):
        self.nosets = self.nosets+1
        self.setarray[v]=self.nosets
    
    def insert(self,v,setno):
        self.setarray[v]=setno

    def merge(self,a,b):
        for i in range(1,len(self.setarray)+1):
            if(self.setarray[i]==b):
                self.setarray[i]=a
