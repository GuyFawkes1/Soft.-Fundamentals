import collections
from graph import *
# start_time = time.time()


def prims(graph_G):
    vertices_no = graph_G.get_vertices()
    vertices_list = list(range(1, vertices_no+1))
    u = [vertices_list[0]]
    T = []
    mst = [[-1 for i in range(0, vertices_no)] for j in range(0, vertices_no)]
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
                        v = temp_list.index(each)+1
                        start = vertex
            mst[start-1][v-1] = max
            cost = cost+max
            u.append(v)
            # print(u)
            T.append((start, v))
            graph_G.cost_matrix[start-1][v-1] = -2
            graph_G.cost_matrix[v-1][start-1] = -2
    print(cost, end=' ')
    graph_R = graph(vertices_no, mst)
    for items in T:
        # print(items)
        graph_R.add_edge(items[0], items[1])
    end_time = float(round(time.time() * 1000, 5))
    print("run time: ", end='')
    print(end_time-start_time, end='')
    # print(end_time-start_time)
    print(')')
    for item in T:
        print(item)
    return graph_G
