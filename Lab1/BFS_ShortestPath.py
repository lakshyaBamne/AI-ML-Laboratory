import math

def bfs_shortest_path(adj_list: list[list], src: int, dest: int) -> list:
    """
        Function to find the shortest path between two nodes in an unweighted
        and undirected graph using Breadth First Search
    """

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
    pred[src] = src

    processing.append(src)

    while len(processing)!=0:
        to_process = processing[0]
        processing.pop()

        for i in adj_list[to_process]:
            if not visited[i]:
                processing.append(i)
                dist[i] = dist[to_process] + 1
                pred[i] = to_process

        if to_process == dest:
            break


    # now using the dist and pred lists we can answer the query