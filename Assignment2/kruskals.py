from Heap import Heap
from Mfset import Mfset
from graph import graph 

def kruskals(graphs):
    
    cost_matrix = [[-1 for i in range(0,graphs.vertices)] for j in range(0,graphs.vertices)]
    mst = graph(graphs.vertices,cost_matrix)
    heap = Heap()
    for i in range(0,graphs.vertices):
        for j in range(i+1,len(graphs.adj[i])):
            if graphs.cost_matrix[i][graphs.adj[i][j]-1] >0:
                heap.insert(i+1,graphs.adj[i][j],graphs.cost_matrix[i][graphs.adj[i][j]-1])

    print(heap.List)

    edgesadd=0
    left = graphs.vertices
    mfset = Mfset(left)
    while(edgesadd<graphs.vertices-1):
        minimum = heap.pop_min()
        print(heap.List)
        
        set1 = mfset.find(minimum[1])
        set2 = mfset.find(minimum[0])

        if set1 == set2:
            if set1 == 0:
                mfset.insertnew(minimum[1])
                mfset.insert(minimum[0],mfset.nosets)
                mst.add_edge(minimum[1],minimum[0])
                mst.cost_matrix[minimum[1]-1][minimum[0]-1]=graphs.cost_matrix[minimum[1]-1][minimum[0]-1]
                mst.cost_matrix[minimum[0]-1][minimum[1]-1]=graphs.cost_matrix[minimum[0]-1][minimum[1]-1]
                edgesadd=edgesadd+1
            else:
                print(mfset.setarray)
                continue
        else:
            if set1 ==0:
                mfset.insert(minimum[1],set2)
                mst.add_edge(minimum[1],minimum[0])
                mst.cost_matrix[minimum[1]-1][minimum[0]-1]=graphs.cost_matrix[minimum[1]-1][minimum[0]-1]
                mst.cost_matrix[minimum[0]-1][minimum[1]-1]=graphs.cost_matrix[minimum[0]-1][minimum[1]-1]
                edgesadd = edgesadd+1
            elif set2 == 0:
                mst.add_edge(minimum[1],minimum[0])
                mst.cost_matrix[minimum[1]-1][minimum[0]-1]=graphs.cost_matrix[minimum[1]-1][minimum[0]-1]
                mst.cost_matrix[minimum[0]-1][minimum[1]-1]=graphs.cost_matrix[minimum[0]-1][minimum[1]-1]
                mfset.insert(minimum[0],set1)    
                edgesadd = edgesadd+1
            else:
                mst.add_edge(minimum[1],minimum[0])
                mst.cost_matrix[minimum[1]-1][minimum[0]-1]=graphs.cost_matrix[minimum[1]-1][minimum[0]-1]
                mst.cost_matrix[minimum[0]-1][minimum[1]-1]=graphs.cost_matrix[minimum[0]-1][minimum[1]-1]
                mfset.merge(set1,set2)
                edgesadd = edgesadd+1
        print(mst.cost_matrix)
        print(mfset.setarray)

    return mst

