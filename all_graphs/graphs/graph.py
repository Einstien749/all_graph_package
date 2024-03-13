"""This Module was developed and being maintained by Odimayo Taiye Moses.  
    It helps mathematicians and curious minds deal with certain problems related to graph theory. 
"""
from itertools import permutations, combinations, product
from copy import deepcopy
class Graph():
    """Class to create an instance of a graph. Since a graph can be defined by its adjacency matrix.
        This class has only one class variable ad_matrix which is a list where it's ith element is the ith
        row of the adjacency matrix.
    """
    def __init__(self, ad_matrix):
        if str(type(ad_matrix))[8:-2] != 'list':
            raise Exception("Adjancency Matrix Must be a list")
        if len(ad_matrix) > 0:
            for i in range(len(ad_matrix)):
                if str(type(ad_matrix[i]))[8:-2] != 'list':
                    raise Exception("Adjancency Matrix Must be a 2D list")
                if len(ad_matrix) == 1 and (len(ad_matrix[0]) != 1):
                    raise Exception("Adjacency Matrix Must Square")
                if (i < (len(ad_matrix) - 1)) and (len(ad_matrix[i]) != len(ad_matrix[i + 1])) and (len(ad_matrix[i]) != len(ad_matrix)):
                    raise Exception("Adjacency Matrix Of A Graph Must Be Square")
        self.ad_matrix = ad_matrix

    def issimple(self):
        """This method test if the graph with the given adjacency matrix is simple. 
        Returns True if it is simple and False if it is not"""
        for i in range(len(self.ad_matrix)):
            if self.ad_matrix[i][i] != 0:
                return False 
            for j in range(len(self.ad_matrix)):
                if (0>self.ad_matrix[i][j]) or (self.ad_matrix[i][j] >= 2):
                    return False
                if self.ad_matrix[i][j] != self.ad_matrix[j][i]:
                    return False
        return True

    def simplify(self):
        """This method returns a simple version of the graph by eliminating loops and multiple edges. 
        """
        if not self.issimple():
            for i in range(len(self.ad_matrix)):
                self.ad_matrix[i][i] = 0
                for j in range(len(self.ad_matrix)):
                    if (i != j) and (self.ad_matrix[i][j] >= 1 or self.ad_matrix[j][i] >= 1):
                        self.ad_matrix[i][j] = 1
                        self.ad_matrix[j][i] = 1
    def iseulerian(self):
        """This method test if the graph with the given adjacency matrix is eulerian graph. 
        Returns True if it is an eulerian graph and False if it is not"""
        if self.issimple() and self.isconnected():
            for i in range(len(self.ad_matrix)):
                if sum(self.ad_matrix[i])%2 != 0:
                    return False
            else:
                return True
        else:
            return False

    def ij_path(self, i, j):
        """This method returns the paths connecting the ith and jth vertices in the graph .
        """
        if (str(type(i))[8:-2] != 'int') and (str(type(j))[8:-2] != 'int'):
            raise Exception("Method Only Accepts Natural Numbers")
        if ((i > len(self.ad_matrix)) or i < 1) and ((j > len(self.ad_matrix)) or j < 1):
            raise Exception("Inputs Are Out Of Range")
        if self.issimple():
            path = []
            other_vert = [m for m in range(len(self.ad_matrix)) if ((m != (i - 1 )) and (m != (j - 1 )))]
            if len(other_vert) > 0:
                for n in range(len(other_vert)):
                    y = list(permutations(other_vert, n + 1))
                    for pit in y:
                        if (self.ad_matrix[i - 1][pit[0]] < 1) or (self.ad_matrix[pit[-1]][j - 1] < 1):
                            continue
                        else:
                            if len(pit) <= 2:
                                if len(pit) == 1:
                                    if i != j:
                                        path.append((i - 1,) + pit + (j - 1,))
                                    else:
                                        continue
                                else:
                                    if self.ad_matrix[pit[0]][pit[-1]] >= 1:
                                        path.append((i - 1,) + pit + (j - 1,))  
                            else:
                                for k in range(len(pit) - 1):
                                    if self.ad_matrix[pit[k]][pit[k + 1]] < 1:
                                        break
                                else:
                                    path.append((i - 1,) + pit + (j - 1,))
            
            if (self.ad_matrix[i - 1][j - 1] >= 1):
                path.append((i - 1,j - 1))
            return path
        else:
            raise Exception("Method Applicable To Simple Graphs Only")
    
    def isconnected(self):
        """ This method test if the graph with the given adjacency matrix is connected.  Returns True if 
        it is connected and False if it is not.
        """
        if len(self.ad_matrix) < 2:
            return False
        else:
            for k in list(combinations([i + 1 for i in range(len(self.ad_matrix))], 2)):
                if len(self.ij_path(*k)) == 0:
                    return False
            else:
                return True
    def istree(self):
        """ This method test if the Graph is a tree. Returns True if it is and False if it is not.
        """
        if len(self.ad_matrix) < 2:
            return False
        else:
            for k in list(combinations([i + 1 for i in range(len(self.ad_matrix))], 2)):
                if len(self.ij_path(*k)) != 1:
                    return False
            else:
                return True
    def deleteedge(self, i, j):
        """This method returns a new graph object by deleting edge ij in the given graph.
        """
        if (str(type(i))[8:-2] != 'int') and (str(type(j))[8:-2] != 'int'):
            raise Exception("Method Only Accepts Natural Numbers")
        if ((i > len(self.ad_matrix)) or i < 1) and ((j > len(self.ad_matrix)) or j < 1):
            raise Exception("Inputs Are Out Of Range")
        if self.issimple():
            if self.ad_matrix[i - 1][j - 1] == 0:
                raise Exception(f"The edge {i}{j} is not in the edge set of the graph")
            else:
                new_admatrix = deepcopy(self.ad_matrix)
                new_admatrix[i - 1][j - 1] = 0
                new_admatrix[j - 1][i - 1] = 0
                return Graph(new_admatrix)
    def contractedge(self, i, j):
        """This method returns a new graph object by contracting edge ij in the given graph.
        """
        if (str(type(i))[8:-2] != 'int') and (str(type(j))[8:-2] != 'int'):
            raise Exception("Method Only Accepts Natural Numbers")
        if ((i > len(self.ad_matrix)) or i < 1) and ((j > len(self.ad_matrix)) or j < 1):
            raise Exception("Inputs Are Out Of Range")
        if self.issimple():
            if self.ad_matrix[i - 1][j - 1] == 0:
                raise Exception(f"The edge {i}{j} is not in the edge set of the graph")
            else:
                new_admatrix = deepcopy(self.ad_matrix)
                for k in range(len(self.ad_matrix)):
                    if (k != i - 1) and (k != j - 1):
                        del new_admatrix[k][max([i - 1, j - 1])]
                        del new_admatrix[k][min([i - 1, j - 1])]
                        new_admatrix[k].append(self.ad_matrix[i - 1][k] + self.ad_matrix[j - 1][k])
                new_admatrix = [new_admatrix[k] for k in range(len(self.ad_matrix)) if (k != i - 1) and (k != j - 1)]
                new_admatrix.append([new_admatrix[k][-1] for k in range(len(new_admatrix))] + [0])
                return Graph(new_admatrix)
        else:
            raise Exception("Method available for simple graphs only")

    def deletevertex(self, v):
        """This method returns a new graph object by deleting the vertex v in the given graph.
        """
        if (str(type(v))[8:-2] != 'int'):
            raise Exception("Method Only Accepts Natural Numbers")
        if ((v > len(self.ad_matrix)) or v < 1):
            raise Exception("Inputs Are Out Of Range")
        if self.issimple():
            new_admatrix = deepcopy(self.ad_matrix)
            del new_admatrix[v - 1]
            for i in range(len(new_admatrix)):
                del new_admatrix[i][v - 1] 
            return Graph(new_admatrix)
        else:
            raise Exception("Method Only Avalaible for simple graphs")
    def isisomorphic(self, obj):
        """ This method test if the graph object(obj) is a subgraph of this Graph. Returns True if 
            it is and False if it is not.
        """
        if str(type(obj))[-7:-2] != 'Graph':
            raise Exception("Method Only Accepts graph object as argument")
        if self.issimple() == False or obj.issimple() == False:
            raise Exception("Both Graphs has to  be simple")
        if len(self.ad_matrix) != len(obj.ad_matrix):
            return False
        else:
            perm = list(permutations(obj.ad_matrix))
            for k in perm:
                no = True
                for i in range(len(self.ad_matrix)):
                    if no:
                        for j in range(len(self.ad_matrix)):
                            if self.ad_matrix[i][j] != k[i][j]:
                                no = False
                                break
                    else:
                        break
                else:
                    return True
            
        return False
    def issubgraph(self, obj):
        if str(type(obj))[-7:-2] != 'Graph':
            raise Exception("Method Only Accepts graph object as argument")
        if self.issimple() == False or obj.issimple() == False:
            raise Exception("Both Graphs has to be simple")
        if len(self.ad_matrix) < len(obj.ad_matrix):
            return False
        else:
            new_mat = deepcopy(obj.ad_matrix)
            if len(self.ad_matrix) > len(obj.ad_matrix):
                for i in range(len(self.ad_matrix) - len(obj.ad_matrix)):
                    new_mat.append([0 for i in range(len(obj.ad_matrix))])
                for k in range(len(self.ad_matrix)):
                    new_mat[k] += [0 for i in range(len(self.ad_matrix) - len(obj.ad_matrix))]
              
            perm = list(permutations(new_mat))
            for k in perm:
                men = list(k)
                g = [[list(k) for k in permutations(men[i])] for i in range(len(men))]
                fm = [list(k) for k in list(product(*tuple(g)))]
                fm = list(fm)
                for my in fm:
                    po = True
                    if Graph(list(my)).issimple():
                        for i in range(len(self.ad_matrix)):
                            for j in range(len(self.ad_matrix)):
                                if self.ad_matrix[i][j] < my[i][j]:
                                    po = False
                                    break
                            if not po:
                                break
                        if po:
                            return True
        return False

    def isdisconnectingset(self, st):
        """This method checks if the set of edges is a disconnecting set of the graph .
           Returns True if it is, else it returns False .
        """
        if str(type(st))[8:-2] != 'list':
            raise Exception("Argument Must be a list")
        if len(st) == 0:
            raise Exception("Argument Must not be empty")
        for a in st:
            if str(type(a))[8:-2] != 'list' and str(type(a))[8:-2] != 'tuple':
                raise Exception("Argument Must be a list of list or of tuples")
            if len(a) != 2:
                raise Exception("Elements of Argument Must be a list or tuple of length 2")
        gcopy = Graph(deepcopy(self.ad_matrix))
        for k in st:
            gcopy = gcopy.deleteedge(*tuple(k))
        if gcopy.isconnected():
            return False
        return True

    def isseparatingset(self, st):
        """This method checks if the set of vertices is a separating set of the graph .
           Returns True if it is else it returns False.
        """
        if str(type(st))[8:-2] != 'list':
            raise Exception("Argument Must be a list")
        if len(st) == 0:
            raise Exception("Argument Must not be empty")
        for a in st:
            if str(type(a))[8:-2] != 'int':
                raise Exception("Argument Must be a list of Natural Numbers")
            if (a > len(self.ad_matrix)) or (a < 1) :
                raise Exception("Vertex Index Out Of Range")
        gcopy = Graph(deepcopy(self.ad_matrix))
        st.sort()
        st.reverse()
        for k in st:
            gcopy = gcopy.deletevertex(k)
        if gcopy.isconnected():
            return False
        return True

    def maximum_connected_subgraph_containing_ith_vertex(self, i):
        """ This method finds the maximum connected subgraph of the graph containing the ith vertex.
            Returns  a new graph object .
        """
        network = deepcopy(self)
        for j in range(1,len(self.ad_matrix) + 1) and (i != j):
            if len(self.ij_path(i,j)) == 0:
                network = network.deletevertex(j)
        return network
