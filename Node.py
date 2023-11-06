class Node:
    def __init__(self, name, price, path, number, is_visited=False) -> None:
        self.name = name
        self.price = price
        self.path = path
        self.is_visited = is_visited
        self.number_of_nodes = number
        self.children = {}

    def add_child(self, name, price):
        child_path = f"{self.path} -> {name}"
        child = Node(name, self.price + price, child_path, self.number_of_nodes + 1)
        self.children[name] = child
        return child