from Node import Node as N 
class Bfs:
    def __init__(self) -> None:
        pass
    def is_goal(city,distonation_name):
        if city.name==distonation_name:
            return False
        return True
    def start_serach (root,distonation_name):
        q=[]
        q.insert(root)
        while is_goal(q.pop,distonation_name):
            
    def print_result(distonation):
            
    
def temp:
    city_queue = Queue()
    city_queue.put(start_city)
    visited[start_city] = True

    while not city_queue.empty():
        current_city = city_queue.get()
        print(city_index[current_city])

        for neighbor_city, distance in enumerate(distance_matrix[current_city]):
            if distance > 0 and not visited[neighbor_city]:
                city_queue.put(neighbor_city)
                visited[neighbor_city] = True

# Main function
if __name__ == "__main__":
    distance_matrix, city_index = create_data()
    start_city = 0  # You can change the start city index as needed
    print("BFS Traversal starting from", city_index[start_city])
    bfs(distance_matrix, start_city)