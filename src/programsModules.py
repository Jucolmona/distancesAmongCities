import networkx as nx

def createGrahpCities(cl, dl):
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

def getCity():
    pass

def getShortestPatch():
    pass

