###########################
###Author: Dustin Martin###
###########################

class Vertex:
    """This is the Vertex class that will be stored and handled by the
       graph class. Each vertex stores it's id and a dictionary of the
       other vertices that it is connected to and the weight of the 
       edge that connects them.
 
    Attributes:
        key: this is the value that identifies the vertex.
   """


    def __init__(self, key):
        """Inits Vertex with a key and empty neighbors list."""
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """Adds a neighbor to the list."""
        self.connectedTo[nbr] = weight

    def __str__(self):
       """Returns a string representation of the class"""
       return str(self.id) + ' connected to: ' + str([x.id for x 
                                                   in self.connectedTo])

    def getConnections(self):
        """Returns all the neighbor's keys."""
        return self.connectedTo.keys()

    def getId(self):
        """Returns vertex id."""
        return self.id

    def getWeight(self, nbr):
        """Reurns the weight of an edge."""
        return self.connectedTo[nbr]


class Graph:
    """This is the Graph ADT class. This class maps a vertex name
       to it's vertex object counter part.
    """

    def __init__(self):
        """Inits graph with a list for vertices and the size of the graph."""
        self.vertList = {}
        self.size = 0

    def addVertex(self, key):
        """Adds a vertex to the graph."""
        self.size = self.size + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """Returns a vertex if it exsists in the graph."""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        """Returns a true if a vertex is in the graph."""
        return n in self.vertList

    def addEdge(self, src, dest, weight=0):
        """Adds an edge between the two given verts with the given weight."""
        if src not in self.vertList:
            newVert = self.addVertex(src)
        if dest not in self.vertList:
            newVert = self.addVertex(dest)
        self.vertList[src].addNeighbor(self.vertList[dest], weight)

    def getVertices(self):
        """Returns the vertices in the graph."""
        return self.vertList.keys()

    def __iter__(self):
       """Returns the Vertex objects of the graph."""
       return iter(self.vertList.values())

