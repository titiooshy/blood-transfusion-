import networkx as nx
import math
from graph_setup import veins
from operator import itemgetter


heart_node = 51


def main_algo():
    """
    Runs the floyd Warshall algorithm
    """
    path_lengths = dict(
        nx.floyd_warshall(veins, weight="weight")
    )  # access the veins globally
    distances_to_heart = {}
    all_nodes = list(veins.nodes())  # extracting the distance to the heart

    for start_node in all_nodes:
        if start_node == heart_node:
            continue

        # comparing the distance to the heart node
        distance = path_lengths.get(start_node, {}).get(heart_node, math.inf)

        if distance != math.inf:
            distances_to_heart[start_node] = distance

    # find the best locations with the quickest path
    if not distances_to_heart:
        min_distance = "N/A (Heart Unreachable)"
        best_sites = {}
    else:
        min_distance = min(distances_to_heart.values())

        best_sites = {
            node: dist
            for node, dist in distances_to_heart.items()
            if dist == min_distance
        }

    best_locations = sorted(best_sites.items(), key=itemgetter(0))
    best_of_ten = sorted(distances_to_heart.items(), key=itemgetter(1))[:10]

    return (min_distance, best_locations, best_of_ten, distances_to_heart)


def display_results(min_distance, sorted_best_sites, top_10_sites, total_distances):
    """Prints the analysis results in a formatted output."""
    # Display all possible paths
    print("\n--- SHORTEST SEGMENTS FOR ALL REACHABLE VERTICES ---")
    all_reachable_vertices = sorted(total_distances.items(), key=itemgetter(0))

    # Display the top ten fastest paths
    print("\n--- TOP 10 CLOSEST INJECTION SITES (Overall) ---")
    if not all_reachable_vertices:
        print("No paths found from any vertex to the heart.")
    else:
        for node, dist in all_reachable_vertices:
            print(f"Vertex {node}: Shortest Path Length = {int(dist)} segments")

    print("\n--- TOP 10 CLOSEST INJECTION SITES (Overall) ---")

    if not top_10_sites:
        print("No paths found to the heart.")
    else:
        # Show the minimum segment count for context
        if isinstance(min_distance, (int, float)):
            print(f"Minimum segments required: {int(min_distance)}")
        # This loop prints the Top 10 overall, sorted by segment length
        for rank, (node, dist) in enumerate(top_10_sites, 1):
            print(f"Rank {rank}: Vertex {node} (Length: {int(dist)} segments)")


# Standard Python execution block
if __name__ == "__main__":
    # Catch the extra return value (all_distances)
    min_dist, best_locations, best_of_ten, all_distances = main_algo()

    # Pass all necessary values to display_results
    display_results(min_dist, best_locations, best_of_ten, all_distances)
