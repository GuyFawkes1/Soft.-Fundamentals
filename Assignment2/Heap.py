class Heap:
    def __init__(self):
        self.List = [(0,0,0)]
        self.last = 0 #effectively a 1 indexed array
    
   
    def insert(self,i,j,w):
        self.List.append((i,j,w))
        self.last = self.last + 1
        lam = self.last
        # swap with its parent until in correct position
        while lam // 2 > 0:
            if self.List[lam][2] < self.List[lam // 2][2]:
                tmp = self.List[lam // 2]
                self.List[lam // 2] = self.List[lam]
                self.List[lam] = tmp
            lam = lam // 2

    def pop_min(self):
        minimum = self.List[1]
        if minimum[2] ==0: #empty-heap
            return (0,0,0)
        
        self.List[1] = self.List[self.last] #replace the first with the last
        self.last = self.last - 1
        self.List.pop()
        i=1
        while (i * 2) <= self.last:
            mc = self.minChild(i)
            if self.List[i][2] > self.List[mc][2]:
                tmp = self.List[i]
                self.List[i]= self.List[mc]
                self.List[mc] = tmp
            i = mc

        return minimum
 
        

    def minChild(self,i):
        if i * 2 + 1 > self.last or self.List[i*2][2] < self.List[i*2+1][2] :
            return i * 2
        else:
            return i * 2 + 1

