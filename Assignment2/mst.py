#import time
import collections
from graph import *
from prims import *


def assignment(cost_matrix):
    n = len(cost_matrix)
    vertices = list(range(1, n+1))
    gr = graph(n, cost_matrix)
    for i in vertices:
        for j in vertices:
            if gr.has_edge(i, j):
                w = cost_matrix[i-1][j-1]
                gr.add_edge(i, j)
    # print(prims(gr))
    print('Prims algorithm MST(total cost: ', end='')
    prims(gr)


'''
cost_matrix = [[0, 6, 1, 5, -1, -1],
               [6, 0, 5, -1, 3, -1],
               [1, 5, 0, 5, 6, 4],
               [5, -1, 5, 0, -1, 2],
               [-1, 3, 6, -1, 0, 6],
               [-1, - 1, 4, 2, 6, 0]]
'''
cost_matrix = [list(map(int, input().split()))]
for index in range(1, len(cost_matrix[0])):
    cost_matrix.append(list(map(int, input().split())))

assignment(cost_matrix)
#end = time.time()
# print(end-start_prim)
