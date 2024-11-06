import networkx as nx

G = nx.Graph()
G.add_node(1)
#Añadir varios nodos a partir de una lista
G.add_nodes_from([2, 3])
#Añadir nodo junto con atributos, los atributos se definen en diccionarios
G.add_nodes_from([(4, {"color":"valor1"}), (5, {"color":"valor2"})])

#Incorporar nodos desde un grafo, hacia otro grafo
H = nx.path_graph(5)
G.add_nodes_from(H)

G.add_nodes_from((11, 'Juan'))

G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)
G.add_edges_from([(1, 3), (2, 4)])

G.clear()

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')
print(G)

