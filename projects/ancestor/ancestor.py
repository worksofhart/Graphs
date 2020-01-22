from graph import Graph


def earliest_ancestor(ancestors, starting_node):

    g = Graph()
    # g is an instance of the class Graph
    for (parent, child) in ancestors:
        g.add_vertex(parent)  # add a vertex from graph.py
        g.add_vertex(child)  # add the second one
    for (parent, child) in ancestors:
        # want to travel UP, so child / parent order
        g.add_edge(child, parent)

    ancestor = g.ancestor_finder(starting_node)

    # Return the ancestor unless the starting node has no parents,
    # In which case return -1
    return ancestor[-1] if len(ancestor) > 1 else -1
