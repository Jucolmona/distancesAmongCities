import networkx as nx

def createGrahpCities(cl:list, dl:list):
    """
    :param cl: Cities List (cl), list-like structure which contain names of cities like nodes
    :param dl: Distances List (dl), list-like structure which contains distances edges among
               two cities (vertices)
    :return: an undirected and weightned grahp of some cities of Colombian
    """
    graphCities = nx.MultiGraph()
    graphCities.add_nodes_from(cl)
    graphCities.add_weighted_edges_from(dl)
    return graphCities
#.................................................................................
def listCities(gc):
    """
    :param gc: graph object that represent the cities
    :return: list which names of cities.
    """
    tmpList = []
    for i in range(1, len(gc.nodes) + 1):
        tmpList.append(gc.nodes[i]['name'])
    return tmpList
#.................................................................................
def matrixRoutes(gc):
    listRoutes = []
    for i, nd in gc.adj.items():
        for n, j in nd.items():
            route = [gc.nodes[i]['name'], gc.nodes[n]['name'], j[0]['weight']]
            listRoutes.append(tuple(route))
    return listRoutes
# .................................................................................
def getCities(gc, tupleString=None):
    """
    :param gc:
    :param tupleString:
    :return:
    """
    namesCities = [gc.nodes[i]['name'] for i in range(1, len(gc.nodes) + 1)]
    if tupleString is not None:
        sg, tg = namesCities.index(tupleString[0]) + 1, namesCities.index(tupleString[1]) + 1
        return sg, tg
# .................................................................................
def getShortestPath(gc, s, t):
    """
    :param gc: Graph Cities, which contains the cities (nodes) and distances (edges) among them 
    :param s: node (means source), starting node of the route
    :param t: node (means target), node target on the route.
    :return: A list, containing the vertices (cities) and edges (distances) that form the shortest path 
    """
    sp = nx.bidirectional_dijkstra(gc, s, t)
    listCities = [gc.nodes[sp[1][i]]['name'] for i in range(len(sp[1]))]
    listDistances = []
    for i in range(len(sp[1]) - 1):
        k = sp[1][i]
        for j in list(gc.adjacency()):
            if j[0] == k:
                for key, value in j[1].items():
                    if sp[1][i + 1] == key:
                        listDistances.append(value[0]['weight'])

    distance = 0.0
    listTable = [(listCities[0], distance)]
    for d in listDistances:
        distance += d
        tupleTmp = tuple([listCities[listDistances.index(d) + 1], distance])
        listTable.append(tupleTmp)
    return listTable
# .................................................................................
def procesingData(gc, tupleRoute):
    citiesIDs = getCities(gc, tupleRoute)
    source = citiesIDs[0]
    target = citiesIDs[1]
    getShortestPath(gc, source, target)
    print("Todo bien !!")