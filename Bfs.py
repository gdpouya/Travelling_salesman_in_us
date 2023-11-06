from datetime import datetime
from Node import Node
class Bfs:
    def __init__(self, root_node, destination_name,distance_matrix, city_index) -> None:
        self.start_time = datetime.now()
        self.root_node = root_node
        self.destination_name = destination_name
        self.number_of_nodes = 1
        self.is_visited=[]
        self.start_search(distance_matrix, city_index)

    def is_goal(self, node):
        return node.name == self.destination_name

    def start_search(self, distance_matrix, city_index):
        queue = [self.root_node]
        while queue:
            current_node = queue.pop(0)
            self.number_of_nodes -= 1
            if current_node.name in self.is_visited:
                pass
            self.is_visited.append(current_node.name)
            if self.is_goal(current_node):
                self.print_result(current_node)
                return

            for child_name, cost in enumerate(distance_matrix[city_index.index(current_node.name)]):
                if cost > 0:
                    child_node = current_node.add_child(city_index[child_name], cost)
                    queue.append(child_node)
                    self.number_of_nodes+=1

        self.print_result(None)
    def dfs_helper(self, current_node):
        self.number_of_nodes += 1

        if self.is_goal(current_node):
            return current_node

        for child in current_node.children:
            result = self.dfs_helper(child)
            if result:
                return result

        return None
    def generate_path(self, destination):
        return destination.path

    def print_result(self, destination_node):
        if destination_node:
            path = self.generate_path(destination_node)
            cost = destination_node.price
            time_elapsed = datetime.now() - self.start_time
            result = f"BFS:\n\t- Cost: {cost}\n\t- Path: {path}\n\t- Number of Nodes in Memory: {self.number_of_nodes}\n\t- Time: {time_elapsed.microseconds} ms"
            print(result)
        else:
            print(f"No path found to {self.destination_name}.")