# Importing in our needed libraries into the code
import networkx as nx
import matplotlib.pyplot as plt

# Initilizting our graph, definition of our graph
G = nx.DiGraph()

# Adding in the final part of the path
# LV-> The start point, Body Part, weight of graph
G.add_edge("LV", "Aorta", weight=1.0)

# List of our nodes
G.add_edge("Aorta", "Art_Kidney", weight=1.8)
G.add_edge("Art_Kidney", "Cap_Kidney", weight=3.0)
G.add_edge("Cap_Kidney", "Vein_Kidney", weight=1.2)  # Dummy Values

# Defining our starting and ending values of our nodes
SOURCE = "LV"
SINK = "LA"

# Implementing shortest path
try:
    # Finds the minimum cumulative weight.
    shortest_path_nodes = nx.shortest_path(
        G, source=SOURCE, target=SINK, weight="weight"
    )
    shortest_path_time = nx.shortest_path_length(
        G, source=SOURCE, target=SINK, weight="weight"
    )
except nx.NetworkXNoPath:
    shortest_path_nodes = []
    shortest_path_time = float("inf")

# Creating the output and printing it out
if shortest_path_nodes:
    path_edges = list(zip(shortest_path_nodes[:-1], shortest_path_nodes[1:]))

    print(f"--- Shortest Path (Minimum Transit Time) Results ---")
    print(f"Path: {' -> '.join(shortest_path_nodes)}")
    print(f"Total Time: {shortest_path_time:.1f} seconds")
else:
    print("No path found between source and sink.")
    path_edges = []
# Make up more positions
pos = 
# Set up node colors
node_colors = 

# Plotting and Visizualution of the paths
plt.figure(figsize=(14, 10))

# Drawing the  nodes
nx.draw_networkx_nodes(
    G, pos, node_color=[node_colors[n] for n in G.nodes()], node_size=3000
)
nx.draw_networkx_labels(G, pos, font_size=9, font_color="black", font_weight="bold")

# Making the edges visisible
nx.draw_networkx_edges(
    G, pos, edge_color="lightgray", arrows=True, alpha=0.6, arrowsize=20
)

# Highlighting the shortest path to a color
nx.draw_networkx_edges(
    G, pos, edgelist=path_edges, edge_color="gold", width=4, arrows=True, arrowsize=30
)
