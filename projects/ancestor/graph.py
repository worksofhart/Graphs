"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # Create an empty Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size():
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                print(v)
                # Mark it as visited
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size():
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Create an empty Set to store visited vertices
        visited = set()

        def traverse(starting_vertex):
            # If the vertex has not been visited
            if starting_vertex not in visited:
                # Mark it as visited
                print(starting_vertex)
                visited.add(starting_vertex)
                # Call traverse for each edge
                for neighbor in self.get_neighbors(starting_vertex):
                    traverse(neighbor)

        traverse(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create an empty Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size():
            # Dequeue the first path
            path = q.dequeue()
            # Look at the last vertex in the path...
            current_vertex = path[-1]
            # And if it is the current vertex, we're done searching
            if current_vertex == destination_vertex:
                return path

            # If the vertex has not been visited
            if current_vertex not in visited:
                # Mark it as visited
                visited.add(current_vertex)
                # Add a path to each neighbor to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    q.enqueue(new_path)

        return None

    def ancestor_finder(self, starting_vertex):
        """
        Modified BFS to find farthest ancestor of starting vertex
        """
        # Create a queue/stack as appropriate
        q = Queue()
        # Put the starting point in that
        q.enqueue([starting_vertex])
        # ^ in an array bc it will be an array w path
        longest_path = [starting_vertex]  # keep track of the longest path
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while q.size():
            # Pop the first item (dequeue)-removes that vertex and returns that vertex
            path = q.dequeue()
            current_vertex = path[-1]
            # If not visited
            if current_vertex not in visited:
                visited.add(current_vertex)
                # For each edge in the item
                for neighbor in self.get_neighbors(current_vertex):
                    # Add that edge to the queue/stack
                    # Make a copy of path rather than reference
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                    # If the new path is longer than current longest, make it the new longest path
                    if len(new_path) > len(longest_path):
                        longest_path = new_path
                    # If equal in length to the longest and its id is less than previous longest's id,
                    # make it the new longest path
                    if len(new_path) == len(longest_path) and new_path[-1] < longest_path[-1]:
                        longest_path = new_path

        return longest_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size():
            # Pop the first path
            path = s.pop()
            # Look at the last vertex in the path...
            current_vertex = path[-1]
            # And if it is the current vertex, we're done searching
            if current_vertex == destination_vertex:
                return path

            # If the vertex has not been visited
            if current_vertex not in visited:
                # Mark it as visited
                visited.add(current_vertex)
                # Add a path to each neighbor to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    s.push(new_path)

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # Create an empty Set to store visited vertices
        visited = set()

        def search(path):
            # Look at the last vertex in the path...
            current_vertex = path[-1]
            # And if it is the current vertex, we're done searching
            if current_vertex == destination_vertex:
                return path
            else:
                # If the vertex has not been visited
                if current_vertex not in visited:
                    # Mark it as visited
                    visited.add(current_vertex)
                    # Call search recursively on each new path
                    for neighbor in self.get_neighbors(current_vertex):
                        if neighbor not in path:
                            # Add a path to each neighbor to the search
                            new_path = path.copy()
                            new_path.append(neighbor)
                            current_path = search(new_path)
                            if current_path is not None:
                                return current_path

        return search([starting_vertex])


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Breadth-first traversal")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Depth-first traversal")
    graph.dft(1)
    print("Depth-first traversal recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Breadth-first search")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Depth-first search")
    print(graph.dfs(1, 6))
    print("Depth-first search recursive")
    print(graph.dfs_recursive(1, 6))
