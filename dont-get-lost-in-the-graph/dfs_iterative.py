from graph import Graph

def dfs_iterative(graph, start_node):
    """Performs an iterative depth-first search (DFS) on a graph.

    Args:
        graph: The Graph object to traverse.
        start_node: The node to start the DFS from.
    """

    stack = [start_node]
    visited = {start_node}

    while stack:
        current_node = stack.pop()
        print(f"Visiting node {current_node}")

        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

if __name__ == '__main__':
    edges = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    graph = Graph(edges)

    print("Depth-First Search (Iterative) starting from node 0:")
    dfs_iterative(graph, 0) 

