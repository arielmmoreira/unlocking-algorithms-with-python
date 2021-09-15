class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, node_from, node_to):
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, node):
        """Insert a Node object in the nodes list"""
        self.nodes.append(Node(node))

    def insert_edge(self, node_from, node_to):
        """Insert an Edge object in the edges list"""
        node_from = node_from
        node_to = node_to
        self.edges.append(Edge(node_from, node_to))

    def get_edge_list(self):
        """Return a list of Edges object"""
        return [edge for edge in self.edges]

    def get_adjacency_list(self):
        adjacencyList = [[] for _ in range(len(self.nodes))]
        for i in range(len(adjacencyList)):
            for edge in self.edges:
                if edge.node_from == i:
                    adjacencyList[i].append(edge.node_to)

        return adjacencyList

    def get_adjacency_matrix(self):
        adjacencyMatrix = [self.get_empty_matrix() for _ in range(len(self.nodes))]
        for i in range(len(adjacencyMatrix)):
            for j in range(len(adjacencyMatrix)):
                for edge in self.edges:
                    if edge.node_from == i:
                        if adjacencyMatrix[i][j] == 0:
                            adjacencyMatrix[i][j] = 1 if edge.node_to == j else 0

        return adjacencyMatrix

    def get_empty_matrix(self):
        matrix = [0] * 14
        return matrix

    def __len__(self):
        return len(self.nodes)