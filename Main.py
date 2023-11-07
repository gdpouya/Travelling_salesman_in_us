from Bfs import Bfs
from DFS import DFS
from UCS import UCS
from Node import Node
from data import create_data
is_debug=True
distance_matrix, city_index = create_data()
if is_debug:
    Start_node_name="New York"
    destination_node_name="Salt Lake City"
else:
    Start_node_name=input("Give me Start city name\n")
    destination_node_name=input("Give me Ddestination city name\n")
root_node = Node(Start_node_name, 0, Start_node_name, 1)
bfs = Bfs(root_node, destination_node_name,distance_matrix, city_index) 
dfs = DFS(root_node,destination_node_name,distance_matrix, city_index)
ucs = UCS(root_node,destination_node_name,distance_matrix, city_index)