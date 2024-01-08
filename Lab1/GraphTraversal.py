import math
from InputGraph import adj_list as graph

class UndirectedGraph:
    """
        Class represents a graph in it's adjacency list representation
        and defines some methods to traverse the graph
    """

    def __init__(self):
        """
            Class constructor
        """


    def bfs(self, adj_list: list[list], src: int) -> list:
        """
            Method to perform bfs from a source node
            returns the order in which the nodes are traversed in a list
        """

        # output list contains the order in which nodes are visited
        traversal_order = []

        # list to keep track of visited nodes
        # initially all the nodes are unvisited
        visited = [False for i in range(len(adj_list))]

        # processing queue
        processing = []

        # start BFS from the source
        visited[src] = True
        processing.append(src)

        while len(processing) != 0:

            # extract the element at the front of the queue
            to_process = processing.pop(0)

            # add the extracted node to the output list
            traversal_order.append(to_process)

            for node in adj_list[to_process]:
                if visited[node] == False:
                    processing.append(node)
                    visited[node] = True

        return traversal_order
    
    def bfs_shortest_path(self, adj_list: list[list], src: int, dest: int) -> list:
        """
            Method to find the shortest path from one node to another using BFS
            -> Time Complexity O(V + E)
        """

        # list to store the shortest path from 
        # source to destination
        shortest_path = []

        # initially all the nodes are unvisited
        visited = [False for i in range(len(adj_list))]

        # processing queue
        processing = []

        # lists to use BFS for finding shortest path
        dist = [math.inf for i in range(len(adj_list))]
        pred = [-1 for i in range(len(adj_list))]

        #! Start BFS from the root
        visited[src] = True
        dist[src] = 0
        processing.append(src)

        while len(processing)!=0:
            to_process = processing.pop(0)

            for i in adj_list[to_process]:
                if not visited[i]:
                    # first two statements are required for BFS to work
                    visited[i] = True
                    processing.append(i)

                    # we need to modify the lists to get the shortest path
                    dist[i] = dist[to_process] + 1
                    pred[i] = to_process

                if i == dest:
                    break

        # now using the dist and pred lists we can answer the query
        chain = dest
        shortest_path.append(dest)
        while pred[chain] != -1:
            shortest_path.insert(0, pred[chain])
            chain = pred[chain]
        return shortest_path

    def dfs(self, adj_list: list[list], src: int) -> list:
        """
            Method to perform dfs on the graph starting from the source node
        """

        # list to store the dfs traversal order
        traversal_order = []

        # visited list to keep track of already visited elements
        visited = [False for i in range(len(adj_list))]

        # processing stack -> add and remove from the back of the list
        processing = []

        # start dfs from the source
        processing.append(src)
        visited[src] = True

        while len(processing) != 0:
            # extract the element at the top of the stack
            to_process = processing.pop()

            # add the extracted element to the output list
            traversal_order.append(to_process)

            for node in adj_list[to_process]:
                if not visited[node]:
                    visited[node] = True
                    processing.append(node)

        return traversal_order

    def dfs_shortest_path(self, adj_list: list[list], src: int, dest: int) -> list:
        """
            Method to find the shortest path between two nodes of a graph using modified DFS
        """

        # list to store the dfs traversal order
        shortest_path = []

        # visited list to keep track of already visited elements
        visited = [False for i in range(len(adj_list))]

        # processing stack -> add and remove from the back of the list
        processing = []

        dist = [math.inf for i in range(len(adj_list))]
        pred = [-1 for i in range(len(adj_list))]

        # start dfs from the source
        processing.append(src)
        visited[src] = True
        dist[src] = 0

        while len(processing) != 0:
            # extract the element at the top of the stack
            to_process = processing.pop()

            for node in adj_list[to_process]:
                if not visited[node]:
                    visited[node] = True
                    processing.append(node)

                    dist[node] = dist[to_process] + 1
                    pred[node] = to_process

                if node == dest:
                    break

        # now we can find the shortest path
        chain = dest
        while pred[chain] != -1:
            shortest_path.insert(0, pred[chain])
            chain = pred[chain]
        shortest_path.append(dest)

        return shortest_path


# instantiate the class to use it's functions
G = UndirectedGraph()

src = 0
dest = 3

# test the BFS function
print(f"BFS order starting from {src} is : {G.bfs(graph, src)}")

# test the DFS function
print(f"DFS order starting from {src} is : {G.dfs(graph, src)}")

# test the shortest path using BFS function
print(f"Shortest path to go from {src} to {dest} (using BFS) is : {G.bfs_shortest_path(graph, src, dest)}")

# test the shortest path using BFS function
print(f"Shortest path to go from {src} to {dest} (using DFS) is : {G.dfs_shortest_path(graph, src, dest)}")
