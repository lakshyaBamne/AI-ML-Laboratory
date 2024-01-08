# Adjacency matrix
adj_mat = []

# Adjacency list
adj_list = [
    [2],
    [2],
    [0,1,4],
    [4],
    [2,3,5],
    [4,6],
    [5]
]

def generate_random_graph(num_of_nodes):
    """
        Function to generate a random graph having given number of nodes
        all the nodes should be points on the xy plane with integral coordinates
        all nodes should be generated in a square with the domain in [-50,50]x[-50,50]
    """
    adj_list = []
