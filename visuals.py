# trying to draw graph
import networkx as nx
import matplotlib.pyplot as plt
from graph_setup import veins


G = veins

F = nx.DiGraph()
F.add_node(33)
F.add_node(34)
F.add_node(35)
F.add_node(36)
F.add_node(37)
F.add_node(182)
F.add_node(51)

F.add_weighted_edges_from(
    [(33, 34, 2), (34, 35, 2), (35, 36, 6), (36, 37, 1), (37, 182, 2), (182, 51, 5)]
)

F.edges[33, 34]["color"] = "red"  # 2

# F.add_edge(34, 35, 2)
F.edges[34, 35]["color"] = "red"  # 2

# F.add_edge(35, 36, 6)
F.edges[35, 36]["color"] = "red"  # 6

# F.add_edge(36, 37, 1)
F.edges[36, 37]["color"] = "red"  # 1

# F.add_edge(37, 182, 2)
F.edges[37, 182]["color"] = "red"  # 2

# F.add_edge(182, 51, 5)
F.edges[182, 51]["color"] = "red"  # 5
F[182][51]["color"] = "red"

nx.draw(F, with_labels=True, font_weight="bold")
# nx.draw(G, with_labels=True, font_weight="bold")
plt.show()
