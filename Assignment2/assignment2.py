import collections
from graph import *
from prims import *
from kruskals import *
import time


def print_graph(Graph):
    x = len(Graph.adj)
    t = []
    for a in range(0, x):
        b = len(Graph.adj[a])
        for c in range(b):
            if (a+1, Graph.adj[a][c]) not in t or (Graph.adj[a][c], a+1) not in t:
                if((Graph.adj[a][c],a+1) not in t):
                    t.append((a+1, Graph.adj[a][c]))
    for edge in t:
        print(edge)

def cost(Graph):
    x = len(Graph.adj)
    t = []
    cost = 0
    for a in range(0, x):
        b = len(Graph.adj[a])
        for c in range(b):
            if (a+1, Graph.adj[a][c]) not in t or (Graph.adj[a][c], a+1) not in t:
                if((Graph.adj[a][c],a+1) not in t):
                    t.append((a+1, Graph.adj[a][c]))
                    cost = cost + Graph.cost_matrix[a][Graph.adj[a][c]-1]

    return cost







def assignment(cost_matrix):
    n = len(cost_matrix)
    vertices = list(range(1, n+1))
    gr = graph(n, cost_matrix)
    for i in vertices:
        for j in vertices:
            #print(gr.has_edge(i, j))
            if gr.has_edge(i, j):
                w = cost_matrix[i-1][j-1]
                gr.add_edge(i, j)

 
    
    start_time = float(round(time.time() * 1000, 5))
    mst_prims = prims(gr)
    end_time = float(round(time.time() * 1000, 5))
    end = end_time-start_time
    print('Prims algorithm MST(total cost: '+str(cost(mst_prims))+'; runtime:'+str(end)+'ms)')
    print_graph(mst_prims)
    
    start_time = float(round(time.time() * 1000, 5))
    mst_krus = kruskals(gr)
    end_time = float(round(time.time() * 1000, 5))
    end = end_time-start_time
    print('Kruskals algorithm MST(total cost: '+str(cost(mst_krus))+'; runtime:'+str(end)+'ms)')
    print_graph(mst_krus)






cost_matrix = [list(map(int, input().split()))]
for index in range(1, len(cost_matrix[0])):
    cost_matrix.append(list(map(int, input().split())))

assignment(cost_matrix)
