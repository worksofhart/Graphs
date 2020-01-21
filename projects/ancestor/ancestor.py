from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Create a new graph
    g = Graph()

    # Add a vertex for each parent and child in ancestors
    for (parent, child) in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)

    # Add an edge for each parent, child pair in ancestors
    for (parent, child) in ancestors:
        g.add_edge(parent, child)

    # Create a new list to store the longest path found
    longest_path = []
    # For each parent node, find a path to the starting node
    for (parent, child) in ancestors:
        path = g.dfs(parent, starting_node)
        # If the path is longer than the previous longest
        # the new path replaces the old one
        if path is not None and len(path) > len(longest_path):
            longest_path = path.copy()

    # Return the ancestor unless the starting node has no parents,
    # In which case return -1
    return longest_path[0] if len(longest_path) > 1 else -1
