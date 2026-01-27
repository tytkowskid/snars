import math
import numpy as np

class Graph:
    vertices: list[int]
    edges: list[tuple[int, int, float]]

    def __init__(self, vertices_n, edges):
        self.vertices = list(range(0, vertices_n))
        self.edges = edges

    def calculate_cords(self):
        points = []
        for i in range(len(self.vertices)):
            ang = 2*math.pi * i/len(self.vertices)
            points.append(np.array([math.cos(ang), math.sin(ang)]))
        
        return points
    
    def get_ar(self):
        return 1

    def v_count(self, v):
        count = 0
        for e in self.edges:
            if (e[0]==v or e[1]==v):
                count += 1
        return count
    
class SquareLattice(Graph):
    n: int
    m: int

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.vertices = list(range(0, n*m))
        edges = []
        for i in range(0, n):
            for j in range(0, m):
                if(j < m-1): edges.append( (i*m + j, i*m + j + 1, 1) )
                if(i < n-1): edges.append( (i*m + j,(i+1)*m + j, 1)  )

        self.edges = edges

    def calculate_cords(self):
        points = []
        for i in range(self.n):
            for j in range(self.m):
                points.append(np.array([j * 1/(self.m-1) - 1/2, 1/(self.n-1) * i - 1/2]) * [2, 2])

        return points
    
    def get_ar(self):
        return (self.m)/(self.n)
    
class CompleteGraph(Graph):
    k: int

    def __init__(self, k):
        self.k = k
        self.vertices = list(range(k))
        self.edges = [(i, j, 1) for i in range(k) for j in range(i+1,k)]

    def calculate_cords(self):
        return super().calculate_cords()