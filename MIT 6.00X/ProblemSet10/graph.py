# 6.00 Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '%s->%s' % (str(self.src), str(self.dest))

class WeightedEdge(Edge):
    #directional weightedEdge
    def __init__(self, src, dest, dist, outdoorDist):
        Edge.__init__(self, src, dest)
        self.distance = dist
        self.odDistance = outdoorDist

    def getDistance(self):
        return self.distance

    def getODDistance(self):
        return self.odDistance

    def __str__(self):
        return str(self.src) + '->(' + str(self.distance) + \
               str(self.odDistance) + ')' + str(self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            #print('duplicate node')
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '%s%s->%s\n' % (res, str(k), str(d))
            #for d in self.edges[k]:
            #    res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph1(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

class Graph(Digraph):
    #edge = weightedEdge
    def getEdges(self):
        return self.edges

    def getNodes(self):
        return self.nodes
    
    def childrenOf(self, motherNode):
        nodes = []
        parentNode = []
        for node in self.nodes:
            if node == motherNode:
                parentNode = node
        for edge in self.edges[parentNode]:
            nodes.append(edge.getDestination())
        return nodes
        #return [nodes for nodes in self.edges[node].getDestination()]
    
    def hasNode(self, node):
        for ele in self.nodes:
            if ele == node:
                return True
        return False
    
    #add Directional Edge
    def addDiEdge(self, weightedEdge):
        src = weightedEdge.getSource()
        dest = weightedEdge.getDestination()
        #for node in self.nodes:
        #    if src == node:
                
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(WeightedEdge(src, dest, \
                                            weightedEdge.getDistance(), \
                                            weightedEdge.getODDistance()))

    #add Bidirectional Edge
    def addBiEdge(self, weightedEdge):
        '''
        src = weightedEdge.getSource()
        dest = weightedEdge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
        '''
        self.addDiEdge(weightedEdge)
        rev = WeightedEdge(weightedEdge.getDestination(), weightedEdge.getSource(),\
                           weightedEdge.getDistance(), weightedEdge.getODDistance())
        self.addDiEdge(rev)

    def __str__(self):
        res = ''
        for k in self.edges:
            if str(k) == '32':
                res += ' '
            for d in self.edges[k]:
                res = '%s%s(%s, %s)->%s\n' % (res, str(k), str(d.getDistance()),\
                                              str(d.getODDistance()), \
                                              str(d.getDestination()))
            #for d in self.edges[k]:
            #    res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]    
                           
def testGraph():
    nodes = []
    for name in range(5):
        nodes.append(Node(str(name)))
    g = Graph()
    for n in nodes:
        g.addNode(n)
    g.addDiEdge(WeightedEdge(nodes[0],nodes[1], 100, 50))
    g.addBiEdge(WeightedEdge(nodes[1],nodes[2], 120, 30))
    g.addBiEdge(WeightedEdge(nodes[2],nodes[0], 80, 10))
    g.addDiEdge(WeightedEdge(nodes[2],nodes[4], 70, 0))
    g.addDiEdge(WeightedEdge(nodes[4],nodes[3], 50, 10))
    return g

def testGraph1():
    nodes = []
    for name in range(5):
        nodes.append(Node(str(name)))
    g = Graph1()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[0]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[4],nodes[3]))
    return g

def printPath(path):
    # a path is a list of nodes
    result = '['
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + '\'' + str(path[i]) + '\']'
        else:
            result = result + '\'' + str(path[i]) + '\', ' 
    return result

