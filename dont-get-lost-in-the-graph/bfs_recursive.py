from collections import deque

# Assuming you have a 'Graph' class defined in 'graph.py'
from graph import Graph

def bfs_recursive(graph, start_node):
    """
    Performs a recursive breadth-first search (BFS) on a graph.

    Args:
        graph: The graph to traverse.
        start_node: The node to start the traversal from.

    Returns:
        None. The function prints the visited nodes in BFS order.
    """

    queue = deque([start_node])
    visited = set([start_node])

    def _bfs_inner():
        """Inner recursive function for BFS traversal."""
        
        if not queue:
            return

        current_node = queue.popleft()
        print(f"Visiting node: {current_node}")

        for neighbor in graph.get_neighbors(current_node):  
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

        _bfs_inner()
    
    _bfs_inner()



if __name__ == '__main__':
    edges = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }

    graph = Graph(edges)

    print("Breadth-First Search starting from node 0:")
    bfs_recursive(graph, 0)