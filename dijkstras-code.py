# Importing in our needed libraries into the code
import networkx as nx
import matplotlib.pyplot as plt
from graph_setup import veins
import time

# setting up all the vertices that a blood transfer can start at
start_time = time.time()  # counting the runtime
heart_node = 51  # final destination
start_vertices = []  # empty matrix

# adding in the needed vertices to the new matrix
for v in range(1, 24):
    start_vertices.append(v)

for v in range(26, 34):
    start_vertices.append(v)

for v in range(52, 81):
    start_vertices.append(v)

for v in range(146, 149):
    start_vertices.append(v)

start_vertices.append(115)
start_vertices.append(116)
start_vertices.append(121)
start_vertices.append(124)
start_vertices.append(116)
start_vertices.append(134)
start_vertices.append(135)
start_vertices.append(126)
start_vertices.append(125)
start_vertices.append(96)
start_vertices.append(184)


def d_algo():
    """
    Runs the dijkstra's algorithm for shortest path to the heart node.

    Args:
        Nothing so far.

    Returns:
        min_distance: The smallest distance from any site to the heart.
        best_locations (list): Vertices that have the shortest distance to the heart.
        best_of_ten (list): The 10 closest vertices overall.
        distances_to_heart (dict): All computed distances from start points to the heart.
    """
    distances_to_heart = {}  # dictionary to store shortest path lengths for each vertex

    # loop through each possible start node
    for start_node in start_vertices:

        # skip to the heart if it happens
        if start_node == heart_node:
            continue

        try:
            # dijkstra’s algorithm to compute the shortest path length along with the weights
            distance = nx.shortest_path_length(
                veins, source=start_node, target=heart_node, weight="weight"
            )
            # storing in the distances
            distances_to_heart[start_node] = distance
        except nx.NetworkXNoPath:
            # skip path it it doesn't go to the heart
            continue

    # if no distances were computed when the heart is unreachable
    if not distances_to_heart:
        min_distance = "N/A (Heart Unreachable)"
        best_sites = {}
    else:
        # the minimum path length
        min_distance = min(distances_to_heart.values())
        best_sites = {
            node: dist
            for node, dist in distances_to_heart.items()
            if dist == min_distance
        }
    # sorted list
    best_locations = sorted(best_sites.items(), key=lambda x: x[0])
    best_of_ten = sorted(distances_to_heart.items(), key=lambda x: x[1])[:10]

    # return statement for computed results
    return min_distance, best_locations, best_of_ten, distances_to_heart


def display_results(min_distance, sorted_best_sites, top_10_sites, total_distances):
    """
    Prints the analysis results in a formatted output.

    Args:
        min_distance: Shortest distance found.
        sorted_best_sites (list): Sites that have the shortest possible distance.
        top_10_sites (list): Top 10 closest injection sites.
        total_distances (dict): Distances for all computed sites.

    Returns:
        Nothing no return statement
    """
    print("\n--- SHORTEST SEGMENTS FOR ALL REACHABLE VERTICES ---")
    all_reachable_vertices = sorted(total_distances.items(), key=lambda x: x[0])

    print("\n--- ALL DISTANCES ---")
    if not all_reachable_vertices:
        print("No paths found from any vertex to the heart.")
    else:
        for node, dist in all_reachable_vertices:
            print(f"Vertex {node}: Shortest Path Length = {int(dist)} segments")

    print("\n--- TOP 10 CLOSEST INJECTION SITES (Overall) ---")

    if not top_10_sites:
        print("No paths found to the heart.")
    else:
        if isinstance(min_distance, (int, float)):
            print(f"Minimum segments required: {int(min_distance)}")
        for rank, (node, dist) in enumerate(top_10_sites, 1):
            print(f"Rank {rank}: Vertex {node} (Length: {int(dist)} segments)")


if __name__ == "__main__":
    # final results
    min_dist, best_locations, best_of_ten, all_distances = d_algo()

    # printed out better
    display_results(min_dist, best_locations, best_of_ten, all_distances)

end_time = time.time()  # record the end time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
