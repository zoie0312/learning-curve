# 6.00 Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#
# Name: 
# Collaborators:
# 

import string
import time
from graph import * #Digraph, Edge, Node

#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph
# A Node represents a building. An WeightedEdge represents the path between two buildings,
# and distance and odDistance of this WeightedEdge represent the distance
# between these 2 buildings and distance between these two buildings that must
# be spent outdoor. As a result, distance >= odDistance.
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    mapfile = open(mapFilename, 'r')
    #nodes = []
    g = Graph()
    for line in mapfile.readlines():
        temp = line.rstrip().split(' ')
        src_node = Node(str(temp[0]))
        des_node = Node(str(temp[1]))
        #if not g.hasNode(src_node):
        addSrc = True
        addDes = True
        for node in g.getNodes():
            if node == src_node:
                addSrc = False
                src_node = node
            if node == des_node:
                addDes = False
                des_node = node
        if addSrc:
            g.addNode(src_node)
        if addDes:
            g.addNode(des_node)
        g.addDiEdge(WeightedEdge(src_node, des_node, int(temp[2]), int(temp[3])))
    #if g.hasNode(Node(str(32))):
    #    print('32 is in')
    #for node in g.nodes:
    #    print(node)
    return g                
        
#testloadmap = load_map('mit_map.txt')
#print(testloadmap)

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
# Minimize traveled distance between two buildings while distance is less than
# or equal to maxTotalDist and distance spent outdoor is less than or equal to
# maxDistOutdoors.

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    #pass
    shortestDistance = maxTotalDist
    shortestPath = []
    if start == end:
        return [start]
    #startNode = Node(start)
    #endNode = Node(end)
    for node in digraph.getNodes():
        if node.getName() == start:
            startNode = node
            #print'found startNode ', start, 'in graph'
        if node.getName() == end:
            endNode = node
            #print'found endNode ', end, 'in graph'
    all_pathes = []
    shortestPath = findAllPathes(digraph, startNode, endNode, maxTotalDist, \
                                 maxDistOutdoors)#[], all_pathes)
    #findAllPathes1(digraph, startNode, endNode, maxDistOutdoors, [], all_pathes)
    '''
    print 'There are ', len(all_pathes), 'pathes in total'
    for path in all_pathes:
        distance, odDistance = pathDistance(path, digraph)
        if distance <= maxTotalDist: #and odDistance <= maxDistOutdoors:
            if distance <= shortestDistance:
                shortestDistance = distance
                shortestPath = path
    '''
    if shortestPath == None:
        #print 'no path found'
        raise ValueError('No Optimal Path Found!! ')
        #return
    else:
        print 'Shortest Path:', printPath(shortestPath)
        return shortestPath
    
    
    
def findAllPathes(graph, start, end, maxDist, maxODDist, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    #pathes = [[]]
    if start == end:
        #print 'PPP'
        #pathes.append(path)
        #print(path)
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or pathTotalDistance(path, graph) <= pathTotalDistance(shortest, graph): 
                newPath = findAllPathes(graph,node,end,maxDist,maxODDist,path)#,pathes)
                if newPath != None:
                    u, v = pathDistance(newPath, graph)
                    if shortest == None or \
                       (u <= maxDist and v <= maxODDist and \
                        u <= pathTotalDistance(shortest, graph)):
                        shortest = newPath
                        #print(shortest)
                        
    return shortest

def findAllPathes1(graph, start, end, maxOdDistance, path = [], pathes = [[]]):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    #pathes = [[]]
    if start == end: #and 
        #print 'PPP'
        #pathes.append(path)
        #print(path)
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = findAllPathes1(graph,node,end,maxOdDistance,path,pathes)
            if newPath != None and newPath not in pathes:
                #u, v = pathDistance(path,graph)
                #print'QQQ'
                #return newPath
                if meetODDistConstraint(newPath, graph, maxOdDistance):
                    pathes.append(newPath)
    return None

def pathDistance(path, graph):
    '''
    Assumes no cycle occured
    Parameters:
    graph: instance of class Digraph or its subclass; represents MIT map
    path: a list of nodes; represents a path from a building to another

    Returns:
    total_dist: total distance traveled
    total_ODdist: total distance spent outdoor
    
    '''
    total_dist = 0
    total_ODdist = 0
    #if len(path) >= 4:
    #    if str(path[0]) == '1' and str(path[1]) == '4' and str(path[2]) == '12' \
    #       and str(path[3]) == '32':
    #        print '1-4-12-32'
    if len(path) <= 1:
        return 0, 0
    for i in range(len(path)-1):
        src_node = Node(str(path[i]))
        des_node = Node(str(path[i+1]))
        for  node in graph.getNodes():
            for edge in graph.getEdges()[node]:
                if edge.getSource() == src_node and edge.getDestination() == des_node:
                    '''
                    if src_node.getName() == '32' and des_node.getName() == '36':
                        print '32->36', edge.getDistance(), edge.getODDistance()
                    if src_node.getName() == '36' and des_node.getName() == '26':
                        print '36->26', edge.getDistance(), edge.getODDistance()
                    if src_node.getName() == '26' and des_node.getName() == '16':
                        print '26->16', edge.getDistance(), edge.getODDistance()
                    if src_node.getName() == '16' and des_node.getName() == '56':
                        print '16->56', edge.getDistance(), edge.getODDistance()
                    if src_node.getName() == '32' and des_node.getName() == '56':
                        print '32->56', edge.getDistance(), edge.getODDistance()
                    if src_node.getName() == '1' and des_node.getName() == '4':
                        print '1->4', edge.getDistance(), edge.getODDistance()
                    if src_node.getName() == '4' and des_node.getName() == '12':
                        print '4->12', edge.getDistance(), edge.getODDistance()
                    if src_node.getName() == '12' and des_node.getName() == '32':
                        print '12->32', edge.getDistance(), edge.getODDistance()
                    '''
                    total_dist += edge.getDistance()
                    total_ODdist += edge.getODDistance()
    #if len(path) == 4:
    #    if str(path[0]) == '1' and str(path[1]) == '4' and str(path[2]) == '12' \
    #       and str(path[3]) == '32':
    #        print 'Path: ', printPath(path), '(',total_dist,' ',total_ODdist, ')'
    return total_dist, total_ODdist    

def meetODDistConstraint(path, graph, maxODDist):
    '''
    Assumes no cycle occured
    Parameters:
    graph: instance of class Digraph or its subclass; represents MIT map
    path: a list of nodes; represents a path from a building to another

    Returns:
    total_dist: total distance traveled
    total_ODdist: total distance spent outdoor
    
    '''
    #total_dist = 0
    total_ODdist = 0
    for i in range(len(path)-1):
        src_node = Node(str(path[i]))
        des_node = Node(str(path[i+1]))
        for  node in graph.getNodes():
            for edge in graph.getEdges()[node]:
                if edge.getSource() == src_node and edge.getDestination() == des_node:
                    #total_dist += edge.getDistance()
                    total_ODdist += edge.getODDistance()
                    if total_ODdist > maxODDist:
                        return False
    #print 'Path: ', printPath(path), '(',total_dist,' ',total_ODdist, ')'
    return True

def meetTotDistConstraint(path, graph, maxDist):
    '''
    Assumes no cycle occured
    Parameters:
    graph: instance of class Digraph or its subclass; represents MIT map
    path: a list of nodes; represents a path from a building to another

    Returns:
    total_dist: total distance traveled
    total_ODdist: total distance spent outdoor
    
    '''
    total_dist = 0
    #total_ODdist = 0
    for i in range(len(path)-1):
        src_node = Node(str(path[i]))
        des_node = Node(str(path[i+1]))
        for  node in graph.getNodes():
            for edge in graph.getEdges()[node]:
                if edge.getSource() == src_node and edge.getDestination() == des_node:
                    total_dist += edge.getDistance()
                    #total_ODdist += edge.getODDistance()
                    if total_ODdist > maxDist:
                        return False
    #print 'Path: ', printPath(path), '(',total_dist,' ',total_ODdist, ')'
    return True


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    #pass
    shortestDistance = maxTotalDist
    shortestPath = []
    if start == end:
        return [start]
    #startNode = Node(start)
    #endNode = Node(end)
    for node in digraph.getNodes():
        if node.getName() == start:
            startNode = node
            #print'found startNode ', start, 'in graph'
        if node.getName() == end:
            endNode = node
            #print'found endNode ', end, 'in graph'
    #all_pathes = []
    #findAllPathes(digraph, startNode, endNode, [], all_pathes)
    shortest_D = maxTotalDist
    shortestPath = dDFSfindShortestPath(digraph, startNode, endNode, \
                                        maxTotalDist, maxDistOutdoors, \
                                        shortest_D,[])
    '''
    for path in all_pathes:
        distance, odDistance = pathDistance(path, digraph)
        if distance <= maxTotalDist: #and odDistance <= maxDistOutdoors:
            if distance <= shortestDistance:
                shortestDistance = distance
                shortestPath = path
    '''

    if shortestPath == None:
        #print 'no path found'
        raise ValueError('No Optimal Path Found!! ')
        #return
    else:
        print 'Shortest Path:', printPath(shortestPath)
        return printPath(shortestPath)

def dDFSfindShortestPath(graph, start, end, maxDist, maxODDist, \
                         shortest_D, path = [], shortest_P = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    #pathes = [[]]
    if start == end: #and 
        #print 'PPP'
        #pathes.append(path)
        #print(path)
        #print(shortest_D)
        #print(shortest_P)
        return path
    u, v = pathDistance(path, graph)
    if u <= maxDist and v <= maxODDist:
        for node in graph.childrenOf(start):
            if node not in path: #avoid cycles
                #u, v = pathDistance(path, graph)
                #if u <= maxDist and v <= maxODDist:
                if shortest_P == None or pathTotalDistance(path, graph) < shortest_D:#u < shortest_D:
                    newPath = dDFSfindShortestPath(graph,node,end,maxDist,\
                                                   maxODDist,shortest_D,path,\
                                                   shortest_P)
                    if newPath != None :
                        u, v = pathDistance(newPath, graph)
                        if u <= maxDist and v <= maxODDist and u <= shortest_D:
                            shortest_P = newPath
                            shortest_D = u
                #u, v = pathDistance(path,graph)
                #print'QQQ'
                #return newPath
                
    #u, v = pathDistance(shortest_P, graph)
    #print(u, v)
    return shortest_P

def pathTotalDistance(path, graph):
    '''
    Assumes no cycle occured
    Parameters:
    graph: instance of class Digraph or its subclass; represents MIT map
    path: a list of nodes; represents a path from a building to another

    Returns:
    total_dist: total distance traveled
    total_ODdist: total distance spent outdoor
    
    '''
    total_dist = 0
    #total_ODdist = 0
    if len(path) <= 1:
        return 0
    for i in range(len(path)-1):
        src_node = Node(str(path[i]))
        des_node = Node(str(path[i+1]))
        for  node in graph.getNodes():
            for edge in graph.getEdges()[node]:
                if edge.getSource() == src_node and edge.getDestination() == des_node:
                    total_dist += edge.getDistance()
                    #total_ODdist += edge.getODDistance()
    #print 'Path: ', printPath(path), '(',total_dist,' ',total_ODdist, ')'
    return total_dist 


# Uncomment below when ready to test
if __name__ == '__main__':
##    # Test cases
    digraph = load_map("mit_map.txt")
##
    LARGE_DIST = 1000000

    # Test case 1
#    print(digraph)
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
#    if digraph.hasNode(Node('32')):
#        print('32 is in')
    t10 = time.time()
    brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    print 'bruteForceSearch took ', (time.time()-t10)*1000, ' ms'
    t11 = time.time()
    dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    print 'directDFSSearch took ', (time.time()-t11)*1000, ' ms'
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
##
##    # Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    t20 = time.time()
    brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
    print 'bruteForceSearch took ', (time.time()-t20)*1000, ' ms'
    t21 = time.time()
    dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
    print 'directDFSSearch took ', (time.time()-t21)*1000, ' ms'
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
##
##    # Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    t30 = time.time()
    brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    print 'bruteForceSearch took ', (time.time()-t30)*1000, ' ms'
    t31 = time.time()
    dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    print 'directDFSSearch took ', (time.time()-t31)*1000, ' ms'
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
##
##    # Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    t40 = time.time()
    brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
    print 'bruteForceSearch took ', (time.time()-t40)*1000, ' ms'
    t41 = time.time()
    dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
    print 'directDFSSearch took ', (time.time()-t41)*1000, ' ms'
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
##
##    # Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    t50 = time.time()
    brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    print 'bruteForceSearch took ', (time.time()-t50)*1000, ' ms'
    t51 = time.time()
    dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    print 'directDFSSearch took ', (time.time()-t51)*1000, ' ms'
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
##
##    # Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    t60 = time.time()
    brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
    print 'bruteForceSearch took ', (time.time()-t60)*1000, ' ms'
    t61 = time.time()
    dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
    print 'directDFSSearch took ', (time.time()-t61)*1000, ' ms'
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
##
    
##    # Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    t70 = time.time()
    try:
        bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    print 'bruteForceSearch took ', (time.time()-t70)*1000, ' ms'
    
    t71 = time.time()
    try:
        directedDFS(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'
    print 'directDFSSearch took ', (time.time()-t71)*1000, ' ms'
##    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
##
##    # Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    t80 = time.time()
    try:
        bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    print 'bruteForceSearch took ', (time.time()-t80)*1000, ' ms'
    
    t81 = time.time()
    try:
        directedDFS(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    print 'directDFSSearch took ', (time.time()-t81)*1000, ' ms'
##    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

