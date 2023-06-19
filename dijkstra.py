import heapq

def dijkstra_algorithm(graph,start,end):
   
    queue = []  # A priority queue to keep track of the nodes to be visited
    heapq.heappush(queue, (0, start))  # Add the start node with distance 0 to the queue
    visited = set()  # A set to keep track of the nodes that have been visited
    distance = {start: 0}  # A dictionary to keep track of the shortest distance to each node
    previous = {}  # A dictionary to keep track of the previous node in the shortest path

    while queue:
        # Get the node with the smallest distance from the start
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            # We have found the shortest path to the end node
            path = [end]
            while previous.get(path[-1]):
                path.append(previous[path[-1]])
            path.reverse()
            output= {'path': path, 'cost': current_distance}
            path_string = ' -> '.join(output['path'])
            return path_string

        if current_node in visited:
            # We have already visited this node, so skip it
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor node
            neighbor_distance = current_distance + weight
            if neighbor not in distance or neighbor_distance < distance[neighbor]:
                # Update the shortest distance to the neighbor node
                distance[neighbor] = neighbor_distance
                # Set the current node as the previous node in the shortest path to the neighbor
                previous[neighbor] = current_node
                # Add the neighbor node to the queue with its distance as priority
                heapq.heappush(queue, (neighbor_distance, neighbor))

    # If we have visited all the nodes and haven't found the end node, there is no path
    return {'path': [], 'cost': float('inf')}




def my_function(graphs,source,destination):
    result = dijkstra_algorithm(graphs,source,destination)
    return result


        
