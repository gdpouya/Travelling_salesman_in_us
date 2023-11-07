from datetime import datetime
from Node import Node
import sys
class UCS:
    def __init__(self, root_node, destination_name,distance_matrix, city_index) -> None:
        self.start_time = datetime.now()
        self.root_node = root_node
        self.destination_name = destination_name
        self.number_of_nodes = 1
        self.distance_matrix=distance_matrix
        self.city_index=city_index
        self.is_visited=[]
        self.start_search(distance_matrix, city_index)

    def is_goal(self, node):
        return node.name == self.destination_name
    
    def go_deep(self,current_node):
        # self.print_result(current_node)
        if current_node.name in self.is_visited:
            self.number_of_nodes -= 1
            return    
        self.is_visited.append(current_node.name)
        if self.is_goal(current_node):
            self.print_result(current_node)
            sys.exit()
        childes=[]
        for child_name, cost in enumerate(self.distance_matrix[self.city_index.index(current_node.name)]):
                if cost > 0 :
                    child=current_node.add_child(self.city_index[child_name], cost)
                    # print(f"cost of {child.name} = {child.price}")
                    childes.append(child)
                    self.number_of_nodes += 1
        
        childes.sort(key=lambda x : x.price)
        for child in childes:
            # print(f"Child cost of {child.name} = {child.price}")
            self.go_deep(child)
        self.number_of_nodes -= 1
    
    def start_search(self, distance_matrix, city_index):
        self.go_deep(self.root_node)
        self.print_result(None)
    
    def generate_path(self, destination):
        return destination.path

    def print_result(self, destination_node):
        if destination_node:
            path = self.generate_path(destination_node)
            cost = destination_node.price
            time_elapsed = datetime.now() - self.start_time
            result = f"UCS:\n\t- Cost: {cost}\n\t- Path: {path}\n\t- Number of Nodes in Memory: {self.number_of_nodes}\n\t- Time: {time_elapsed.microseconds} ms"
            print(result)
        else:
            print(f"No path found to {self.destination_name}.")