from graphs import Graph
from math import pi, tan

class WeightedGraph(Graph):
    """Class to create an instance of a Weighted Graph. Hence extends the Graph class. It has additional class
        variable weights which is a list with same dimension as the adjacency matrix."""
    def __init__(self, ad_matrix, weights):
        super().__init__(ad_matrix)
        if str(type(weights))[8:-2] != 'list':
            raise Exception("Weight Matrix Must be a list")
        if len(weights) > 0:
            for i in range(len(weights)):
                if str(type(weights[i]))[8:-2] != 'list':
                    raise Exception("Weight Matrix Must be a 2D list")
                if len(weights) == 1 and (len(weights[0]) != 1):
                    raise Exception("Weight Matrix Must Square")
                if (i < (len(weights) - 1)) and (len(weights[i]) != len(weights[i + 1])) and (len(weights[i]) != len(weights)):
                    raise Exception("Weight Matrix Of A Graph Must Be Square")
        if len(weights) != len(self.ad_matrix):
            raise Exception("Weight Matrix Must be of the same dimension as adjacency matrix")
        for j in range(len(self.ad_matrix)):
            if (len(self.ad_matrix[j])) != (len(weights[j])):
                raise Exception("Weight Matrix Must be of the same dimension as adjacency matrix")
            for i in range(len(self.ad_matrix)):
                if (self.ad_matrix[j][i] == 0) and (weights[j][i] != 0):
                    raise Exception("Such edge doesn't exist in the graph") 
        self.weights = weights
    def maxpathbyweight(self, i, j):
        """ This method finds the weight of the path with maximum total weight connecting the ith vertex to the jth vertex.
            Returns  a natural number greater than 0 if it finds a path, and 'No path' if no path exists,.
        """
        pol = 0
        if len(super().ij_path(i, j)) > 0:
            for n in super().ij_path(i, j):
                sum_path = 0
                for k in range(len(n) - 1):
                    sum_path += self.weights[n[k]][n[k+1]]
                if sum_path >= pol:
                    pol = sum_path
            return pol
        return 'No path'

    def minpathbyweight(self, i, j):
        """ This method finds the weight of the path with minimum total weight connecting the ith vertex to the jth vertex.
            Returns  a natural number greater than 0 if it finds a path, and 0 if no path exists,.
        """
        pol = tan(pi/2)
        if len(super().ij_path(i, j)) > 0:
            for n in super().ij_path(i, j):
                sum_path = 0
                for k in range(len(n) - 1):
                    sum_path += self.weights[n[k]][n[k+1]]
                if sum_path < pol:
                    pol = sum_path
            return pol
        return 'No path'
