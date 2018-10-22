import collections


class graph():
    def __init__(self, vertices, cost_matrix):
        self.vertices = vertices
        self.cost_matrix = cost_matrix
        self.adj = [[] for z in range(self.vertices)]

    def has_edge(self, vertex1, vertex2):
        if self.cost_matrix[vertex1-1][vertex2-1] > 0:
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        # self.cost_matrix[vertex1-1][vertex2-1]=self.cost_matrix[vertex1-1][vertex2-1]+weight
        temp1 = self.adj[vertex1-1]
        if vertex2 not in temp1:
            temp1.append(vertex2)
        temp2 = self.adj[vertex2-1]
        if vertex1 not in temp2:
            temp2.append(vertex1)

    def cost(self):
        cost = 0
        for i in range(0,vertices):
            for j in range(0,len(adj[i])):
                if cost_matrix[i][adj[i][j]]>0:
                    cost = cost+cost_matrix[i][adj[i][j]]
        return cost


    def print(self):
        for i in range(0,vertices):
            for j in range(0,len(adj[i])):
                print((i,adj[i][j]))


    def get_vertices(self):
        return self.vertices

    def __return__(self):
        return self.adj
