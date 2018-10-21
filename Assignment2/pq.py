class Heap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
   
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        i = self.currentSize
        # swap with its parent until in correct position
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
            