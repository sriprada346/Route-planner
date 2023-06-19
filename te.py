import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance = float('inf')
        self.visited = False
        self.previous = None
        
    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

class Graph:
    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        self.nodes.add(node)

    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None 

def dijkstra(graph, start, end):
    start_node = graph.find_node(start)
    end_node = graph.find_node(end)

    start_node.distance = 0
    unvisited = [(node.distance, node) for node in graph.nodes]
    heapq.heapify(unvisited)

    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.name)
                current_node = current_node.previous
            return path[::-1]

        current_node.visited = True

        for neighbor, weight in current_node.neighbors.items():
            if not neighbor.visited:
                new_distance = current_node.distance + weight
                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    neighbor.previous = current_node
                    for i in range(len(unvisited)):
                        if unvisited[i][1] == neighbor:
                            unvisited[i] = (new_distance, neighbor)
                            break
                    heapq.heapify(unvisited)
    return None

graph = Graph()

bank = Node('bank')
canteen = Node('canteen')
cvraman = Node('cvraman')
ramanujan = Node('ramanujan')
sanmathi = Node('sanmathi')
bustand = Node('busstand')

graph.add_node(bank)
graph.add_node(canteen)
graph.add_node(cvraman)
graph.add_node(ramanujan)
graph.add_node(sanmathi)
graph.add_node(bustand)

bank.add_neighbor(canteen, 2)
bank.add_neighbor(canteen, 1)
canteen.add_neighbor(bank, 2)
canteen.add_neighbor(cvraman, 3)
canteen.add_neighbor(ramanujan, 5)
cvraman.add_neighbor(canteen, 3)
cvraman.add_neighbor(ramanujan, 2)
sanmathi.add_neighbor(canteen, 5)
ramanujan.add_neighbor(cvraman, 2)
ramanujan.add_neighbor(sanmathi, 1)
bustand.add_neighbor(ramanujan, 1)
sanmathi.add_neighbor(bustand, 2)


source_node_names = ["bank", "canteen", "cvraman", "ramanujan", "sanmathi", "busstand"]
source_node_numbers = {source_node_names[i]: i+1 for i in range(len(source_node_names))}

def shortest_path():
    #source_number = source_node_numbers[source]
    #destination_number = source_node_numbers[destination]
    #path = dijkstra(graph, source_number, destination_number)
   # return path

# Example usage
    print(shortest_path("bank", "busstand"))
