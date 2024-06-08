class Graph:
    """Represents a graph data structure using an adjacency list."""
    
    def __init__(self, edges):
        """
        Initializes a new graph.

        Args:
            edges: A dictionary where keys are nodes and values are lists of their neighboring nodes.
        """
        self.adjacency_list = edges  # Dictionary: {node: [neighbor1, neighbor2...]}

    def get_neighbors(self, node):
        """
        Gets the neighbors of a given node.

        Args:
            node: The node to get neighbors for.

        Returns:
            A list of neighboring nodes, or an empty list if the node is not found.
        """
        return self.adjacency_list.get(node, [])
