"""
Created on Mon Apr 11 23:28:21 2016

@author: nachiketbhagwat
"""

from collections import deque

class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v  
        self.capacity = w
        self.previous = None
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork(object):
    def __init__(self):
        self.adj = {} # adjacency network
        self.flow = {} # flow network
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []#For every vertex maintain adjecancy list
 
    def get_edges(self, v):
        return self.adj[v] #return adjusancy list for all vertices
 
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w) #forward edge with capacity max W, which can be changed later
        redge = Edge(v,u,0) #backward edge with capacity 0, which can be changed later
        edge.redge = redge #reverse edges
        redge.redge = edge#reverse edges
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path_bfs(self, source, sink, path):
        visited = {}
        queue = deque([])
        final_edge = None
        pathFound = False
        
        for edge in self.get_edges(source):#source edges
            residual = edge.capacity - self.flow[edge]#residual capacity
            edge.previous = None
            if residual > 0 and visited.has_key(edge.sink) == False:#valid unvisited node+edge
                if edge.sink == sink:#sink reached in first step
                        pathFound = True
                        final_edge= edge
                        break
                queue.append(edge)#path appended with edge to return
        
        while(len(queue)>0 and pathFound == False):
            curEdge = queue.popleft()#queue implementation
            vertex = curEdge.sink
            visited[vertex] = 1
                
            for newEdge in self.get_edges(vertex):
                residual = newEdge.capacity - self.flow[newEdge]#residual capacity
                if residual > 0 and visited.has_key(newEdge.sink) == False:#valid unvisited node+edge
                    if newEdge.sink == sink:
                        pathFound = True
                        final_edge = curEdge
                        break
                    else:
                        newEdge.previous = curEdge
                        queue.append(newEdge)
                        
        if pathFound == True:
            path.insert(0,final_edge)
            final_edge = final_edge.previous

            while(final_edge != None):
                path.insert(0,final_edge)
                final_edge = final_edge.previous
                
        return path
        
    def max_flow(self, source, sink):
        path = self.find_path_bfs(source, sink, [])
        print path
        count = 1
        while path != []:
            #print path
            count = count + 1
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path_bfs(source, sink, [])
        print "iterations: "+ str(count)    
        return sum(self.flow[edge] for edge in self.get_edges(source))