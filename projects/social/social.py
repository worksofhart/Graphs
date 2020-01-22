from util import Queue
import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # # Create friendships
        # # total_friendships = avg_friendships * num_users
        # # Generate a list of all possible friendships
        # possible_friendships = []
        # # Avoid duplicates by ensuring the first ID is smaller than the second
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))

        # # Shuffle the list
        # random.shuffle(possible_friendships)

        # # print(possible_friendships)

        # # Slice off excess friendships, add edge to the remaining
        # # add_friendship will be called avg_friendships * num_users / 2 times
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

        for i in range(num_users * avg_friendships // 2):
            user_id1 = random.randint(1, self.last_id - 1)
            user_id2 = random.randint(user_id1 + 1, self.last_id)
            self.add_friendship(user_id1, user_id2)

    def get_friends(self, user_id):
        """
        Get all friends (edges) of a user.
        """
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # Create an empty Set to store visited vertices
        visited = {}

        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([user_id])

        # While the queue is not empty...
        while q.size():
            # Dequeue the first path
            path = q.dequeue()
            # Look at the last user in the path...
            current_friend = path[-1]

            # If the user has not been visited
            if current_friend not in visited:
                # Mark as visited and add their path
                visited[current_friend] = path
                # Add a path to each neighbor to the queue
                for friend in self.get_friends(current_friend):
                    new_path = path.copy()
                    new_path.append(friend)
                    q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    print()
    MANY_USERS_TOTAL = 10000
    many_users = SocialGraph()
    many_users.populate_graph(MANY_USERS_TOTAL, 5)
    many_connections = many_users.get_all_social_paths(1)
    print(many_connections)
    total_connections = len(many_connections)
    print(
        f"User 1 is connected to {100 * total_connections / MANY_USERS_TOTAL}% of members")
    all_path_lengths = sum(len(p) for p in many_connections.values())
    avg_degrees_of_separation = all_path_lengths / total_connections
    print(
        f"With an average of {avg_degrees_of_separation} degrees of separation")
