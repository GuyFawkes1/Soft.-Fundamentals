import Heap
import Mfset
import graph

def kruskals(graphs):
    mst = graph()
    cost_matrix = [[-1 for i in range(0,graphs.vertices)] for j in range(0,graphs.vertices)]
    heap = Heap()
    for i in range(0,graphs.vertices):
        for j in range(0,len(graphs.adj[i])):
            heap.insert(i+1,graphs.adj[i][j],graphs.cost_matrix[i][graphs.adj[i][j]-1])

    completed=0
    left = graphs.vertices
    mfset = Mfset(left)
    while(left>0):
        minimum = heap.pop_min()
        set1 = mfset.find(minimum[1])
        set2 = mfset.find(minimum[2])

        if set1 == set2:
            if set1 == 0:
                mfset.insertnew(minimum[1])
                mfset.insertnew(minimum[2])
                mst.add_edge(minimum[1],minimum[2])
                mst.cost_matrix[minimum[1]-1][minimum[2]-1]=graphs.cost_matrix[minimum[1]-1][minimum[2]-1]
                mst.cost_matrix[minimum[2]-1][minimum[1]-1]=graphs.cost_matrix[minimum[2]-1][minimum[1]-1]
                left=left-2
            else:
                continue
        else:
            if set1 ==0:
                mfset.insert(minimum[1],set2)
                mst.add_edge(minimum[1],minimum[2])
                mst.cost_matrix[minimum[1]-1][minimum[2]-1]=graphs.cost_matrix[minimum[1]-1][minimum[2]-1]
                mst.cost_matrix[minimum[2]-1][minimum[1]-1]=graphs.cost_matrix[minimum[2]-1][minimum[1]-1]
                left=left-1
            elif set2 == 0:
                mst.add_edge(minimum[1],minimum[2])
                mst.cost_matrix[minimum[1]-1][minimum[2]-1]=graphs.cost_matrix[minimum[1]-1][minimum[2]-1]
                mst.cost_matrix[minimum[2]-1,minimum[1]-1]=graphs.cost_matrix[minimum[2]-1][minimum[1]-1]
                mfset.insert(minimum[2],set1)    
                left=left-1
            else:
                mst.add_edge(minimum[1],minimum[2])
                mst.cost_matrix[minimum[1]-1][minimum[2]-1]=graphs.cost_matrix[minimum[1]-1][minimum[2]-1]
                mst.cost_matrix[minimum[2]-1][minimum[1]-1]=graphs.cost_matrix[minimum[2]-1][minimum[1]-1]
                merge(set1,set2)

    return mst

