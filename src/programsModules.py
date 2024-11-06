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

def listCities(gc):
    """
    :param gc: graph object that represent the cities
    :return: list which names of cities.
    """
    for i in range(1, len(gc.nodes) + 1):
        print(gc.nodes[i]['name'])

def listDistances():
    pass

def getCity():
    pass

def getShortestPatch():
    pass