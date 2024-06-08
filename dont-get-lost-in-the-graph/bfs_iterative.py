from collections import deque
from graph import Graph


def bfs_iterative(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) iteratively through the graph.

    Args:
        graph: The graph object to traverse.
        start_node: The node to start the search from.

    Returns:
        None: Prints the nodes as they are visited.
    """

    queue = deque([start_node])
    visited = {start_node}

    while queue:
        current_node = queue.popleft()
        print(f"Visiting node: {current_node}")

        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


if __name__ == "__main__":
    edges = {0: [1, 2], 1: [3], 2: [3], 3: []}

    graph = Graph(edges)

    print("Breadth-First Search starting from node 0:")
    bfs_iterative(graph, 0)
