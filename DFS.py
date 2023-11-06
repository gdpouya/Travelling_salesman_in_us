from datetime import datetime
from Node import Node
import sys
class DFS:
    def __init__(self, root_node, destination_name,distance_matrix, city_index):
        self.start_time = datetime.now()
        self.root_node = root_node
        self.destination_name = destination_name
        self.number_of_nodes = 1
        self.is_visited=[]
        self.distance_matrix=distance_matrix
        self.city_index=city_index
        self.start_search()
        
    def is_goal(self, node):
        # print(f"check goal{node.name}")
        return node.name == self.destination_name
    def dfs_go(self,current_node):
        if current_node.name in self.is_visited:
            self.number_of_nodes -= 1
            return    
        self.is_visited.append(current_node.name)
        if self.is_goal(current_node):
            self.print_result(current_node)
            sys.exit()
        for child_name, cost in enumerate(self.distance_matrix[self.city_index.index(current_node.name)]):
                if cost > 0 and self.city_index[child_name]:
                    child_node = current_node.add_child(self.city_index[child_name], cost)
                    self.number_of_nodes += 1
                    self.dfs_go(child_node)
        self.number_of_nodes -= 1
        
    def start_search(self):
        self.dfs_go(self.root_node)
        self.print_result(None)

    def generate_path(self, destination):
        return destination.path

    def print_result(self, destination_node):
        if destination_node:
            path = self.generate_path(destination_node)
            cost = destination_node.price
            time_elapsed = datetime.now() - self.start_time
            result = f"DFS:\n\t- Cost: {cost}\n\t- Path: {path}\n\t- Number of Nodes in Memory: {self.number_of_nodes}\n\t- Time: {time_elapsed.microseconds} ms"
            print(result)
        else:
            print(f"No path found to {self.destination_name}.")