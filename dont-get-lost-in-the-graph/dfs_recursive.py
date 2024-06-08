from graph import Graph

def dfs_recursive(graph, start_node, visited=None):
    """
    Performs a Depth-First Search (DFS) traversal of the graph recursively.

    Args:
        graph: The Graph object to traverse.
        start_node: The node to begin the DFS traversal from.
        visited (set, optional): A set to track visited nodes. Defaults to None.
    """

    visited = visited or set()
    visited.add(start_node)     
    print(f"Visiting node: {start_node}")

    for neighbor in graph.get_neighbors(start_node):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


if __name__ == '__main__':
    edges = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }

    graph = Graph(edges)

    print("Depth-First Search starting from node 0:")
    dfs_recursive(graph, 0)
