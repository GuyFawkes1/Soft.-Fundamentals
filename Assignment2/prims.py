import collections
from graph import *


def prims(graph_G):
    vertices_no = graph_G.get_vertices()
    vertices_list = list(range(1, vertices_no+1))
    u = [vertices_list[0]]
    T = []
    mst_cost_matrix = [[-1 for i in range(0, vertices_no)] for j in range(0, vertices_no)]
    cost = 0
    while len(u) <= len(vertices_list):
        if len(u) == len(vertices_list):
            break
        else:
            max = 100
            v = 0
            start = 0
            for vertex in u:
                temp_list = graph_G.cost_matrix[vertex-1]
                for i in range(len(temp_list)):
                    if temp_list[i] > 0 and temp_list[i] < max and (i+1) not in u:
                        max = temp_list[i]
                        v = (i+1)
                        start = vertex
            cost = cost+max
            u.append(v)
            mst_cost_matrix[start-1][v-1] = max
            mst_cost_matrix[v-1][start-1] = max

            T.append((start, v))

       
    
    graph_R = graph(vertices_no, mst_cost_matrix)
    for key in T:
     
        graph_R.add_edge(key[0], key[1])
    
    return graph_R
