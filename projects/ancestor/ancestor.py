from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Create a new graph
    g = Graph()

    # Add a vertex and edge for each parent and child in ancestors
    for (parent, child) in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(parent, child)
