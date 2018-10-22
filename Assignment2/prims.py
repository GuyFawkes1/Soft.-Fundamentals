import collections
from graph import *
import time
# start_time = time.time()
start_time = float(round(time.time() * 1000, 5))


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
                # print(graph_G.cost_matrix[u-1])
                # print(type(graph_G.cost_matrix[u-1]))
                temp_list = graph_G.cost_matrix[vertex-1]

                for each in temp_list:
                    if each > 0 and each < max and temp_list.index(each)+1 not in u:
                        max = each
                        v = (temp_list.index(each)+1)
                        start = vertex
            '''
            for each_item in v:
                if each_item not in u:
                    u.append(each_item)
                    T.append((start, each_item))
                    mst_cost_matrix[start-1][each_item-1] = max
                    mst_cost_matrix[each_item-1][start-1] = max
            '''
            cost = cost+max
            u.append(v)
            mst_cost_matrix[start-1][v-1] = max
            mst_cost_matrix[v-1][start-1] = max
            # print(u)
            T.append((start, v))

            # print(T)
            #graph_G.cost_matrix[start-1][v-1] = -2
            #graph_G.cost_matrix[v-1][start-1] = -2
    # print(mst_cost_matrix)
    print(cost, end=' ')
    graph_R = graph(vertices_no, mst_cost_matrix)
    for x, y in T:
        # print(items)
        # print(x)
        # print(y)
        graph_R.add_edge(x, y)
    end_time = float(round(time.time() * 1000, 5))
    print("run time: ", end='')
    print(end_time-start_time, end='')
    # print(end_time-start_time)
    print(')')
    #print(graph_R.adj[0])
    return graph_R
