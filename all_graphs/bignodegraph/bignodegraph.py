"""This Module was developed and being maintained by Odimayo Taiye Moses.  
    It helps mathematicians and curious minds deal with certain problems related to graph theory. 
"""
from graphs import Graph
from copy import deepcopy
class BigNodeGraph():
    """Class to create an instance of a graph with a large amount of nodes(vertices) is very large compared to the number of edges. This class has two class variables ad_edges which is a list of tuples repesenting an edge of the graph,
       and a natural number reprsenting the number of nodes.
    """
    def __init__(self, ad_edges, n):
        if str(type(ad_edges))[8:-2] != 'list':
            raise Exception("Edge Set Must be a list")
        if len(ad_edges) > 0:
            for i in range(len(ad_edges)):
                if str(type(ad_edges[i]))[8:-2] != 'tuple':
                    raise Exception("An edge of the graph is a tuple .")
                if len(ad_edges[0]) != 2:
                    raise Exception("Edges Must Be Tuples")
                if str(type(ad_edges[0][0]))[8:-2] != 'int' or str(type(ad_edges[0][1]))[8:-2] != 'int' :
                    raise Exception("Labels On Graph Vertices Are Natural Numbers")
                if 1>ad_edges[0][0]>n or 1>ad_edges[0][1]>n :
                    raise Exception("Labels On Graph Vertices Out Of Range")
        ad_matrix = []
        for i in range(n):
            ad_matrix.append([0 for j in range(n)])
        for h in ad_edges:
            ad_matrix[h[0] - 1][h[1] - 1] = 1
            ad_matrix[h[1] - 1][h[0] - 1] = 1
        
        super().__init__(ad_matrix)