#import time
import collections
from graph import *
from prims import *
from kruskals import *


def assignment(cost_matrix):
    n = len(cost_matrix)
    vertices = list(range(1, n+1))
 #   print(cost_matrix)
    gr = graph(n, cost_matrix)
    
    for i in vertices:
        for j in vertices:
            if gr.has_edge(i, j):
                print((i,j))
                gr.add_edge(i, j)

    print(gr.adj[1])

 
    print('Prims algorithm MST(total cost: ', end='')
    # prims(gr)
    # gr.cost_matrix = cost_matrix
    mst_krus = kruskals(gr)
    print(mst_krus.cost_matrix)



cost_matrix = [[0, 6, 1, 5, -1, -1],
               [6, 0, 5, -1, 3, -1],
               [1, 5, 0, 5, 6, 4],
               [5, -1, 5, 0, -1, 2],
               [-1, 3, 6, -1, 0, 6],
               [-1, - 1, 4, 2, 6, 0]]

# cost_matrix = [list(map(int, input().split()))]
# for index in range(1, len(cost_matrix[0])):
#     cost_matrix.append(list(map(int, input().split())))

assignment(cost_matrix)
#end = time.time()
# print(end-start_prim)
