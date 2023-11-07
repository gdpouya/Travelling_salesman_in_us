#Graph Search Algorithms
This repository contains Python implementations of various graph search algorithms, including Breadth-First Search (BFS), Depth-First Search (DFS), and Uniform Cost Search (UCS). These algorithms are applied to find paths in a graph from a start node to a destination node. The project consists of the following files:

1. bfs.py
Overview
This script defines the BFS (Breadth-First Search) class, which implements the Breadth-First Search algorithm to find the shortest path in a graph.

Features
Implements BFS algorithm for graph traversal.
Utilizes a queue for efficient exploration of nodes.
Prints the resulting path, cost, number of nodes in memory, and the time elapsed.
Usage
python
Copy code
# Example usage of BFS algorithm
from bfs import BFS, Node, create_data

# Create data (distance_matrix, city_index)
distance_matrix, city_index = create_data()

# Initialize BFS with root_node, destination_node_name, distance_matrix, and city_index
bfs = BFS("New York", "Salt Lake City", distance_matrix, city_index)

# Start BFS search
bfs.start_search()
2. dfs.py
Overview
This script defines the DFS (Depth-First Search) class, which implements the Depth-First Search algorithm to find a path in a graph.

Features
Implements DFS algorithm for graph traversal.
Utilizes recursive depth-first exploration of nodes.
Prints the resulting path, cost, number of nodes in memory, and the time elapsed.
Usage
python
Copy code
# Example usage of DFS algorithm
from dfs import DFS, Node, create_data

# Create data (distance_matrix, city_index)
distance_matrix, city_index = create_data()

# Initialize DFS with root_node, destination_node_name, distance_matrix, and city_index
dfs = DFS("New York", "Salt Lake City", distance_matrix, city_index)

# Start DFS search
dfs.start_search()
3. ucs.py
Overview
This script defines the UCS (Uniform Cost Search) class, which implements the Uniform Cost Search algorithm to find the shortest path in a graph.

Features
Implements UCS algorithm for finding the shortest path in a graph.
Utilizes priority queue for efficient exploration based on node cost.
Prints the resulting path, cost, number of nodes in memory, and the time elapsed.
Usage
python
Copy code
# Example usage of UCS algorithm
from ucs import UCS, Node, create_data

# Create data (distance_matrix, city_index)
distance_matrix, city_index = create_data()

# Initialize UCS with root_node, destination_node_name, distance_matrix, and city_index
ucs = UCS("New York", "Salt Lake City", distance_matrix, city_index)

# Start UCS search
ucs.start_search()
4. node.py
Overview
This script contains the Node class, representing a node in a graph. It provides methods to add child nodes and store relevant information.

Node Class Attributes
name: The name or identifier of the node.
price: The accumulated cost or price to reach the node.
path: The path from the root node to this node.
is_visited: A flag indicating whether the node has been visited or not. Default is False.
number_of_nodes: The number of nodes in the path to this node.
children: A dictionary of child nodes, where the keys are the names of the child nodes and the values are the corresponding child node objects.
Methods
__init__(self, name, price, path, number, is_visited=False): Constructor method to initialize a Node object with the provided attributes.
add_child(self, name, price): Adds a child node to the current node and returns the newly created child node.
Usage
python
Copy code
# Example usage of Node class
from node import Node

# Create a root node
root = Node("A", 0, "A", 1)

# Add child nodes
root.add_child("B", 10)
root.add_child("C", 20)

# Access child nodes
child_b = root.children["B"]
child_c = root.children["C"]
Running the Algorithms
To run any of the algorithms, import the corresponding class and create instances with appropriate parameters, such as root_node, destination_node_name, distance_matrix, and city_index. Then, call the respective start_search() method to initiate the search.

Feel free to reach out if you have any questions or need further assistance with the implementation or usage of these algorithms. Happy coding!