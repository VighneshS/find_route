import sys
from queue import PriorityQueue

links_file_name = sys.argv[1]
start_state = sys.argv[2]
goal_state = sys.argv[3]


def expand_node(node_to_expand, fringe, traversal, total_generated, heuristic):
    generated = total_generated
    for link in links[node_to_expand[1]]:
        cumulative_cost = links[node_to_expand[1]][link] + traversal[node_to_expand[1]][1]
        fringe.put((cumulative_cost + heuristic[link] if heuristic else cumulative_cost, link))
        generated += 1
        if link not in traversal:
            traversal[link] = (node_to_expand, cumulative_cost)
    return generated


def get_cost_and_path_of_traversal(traversal, destination, origin):
    path = []
    cumulative_cost = "Infinity"
    if destination in traversal:
        cumulative_cost = 0.0
        node = destination
        while node != origin:
            sub_path_cost = links[traversal[node][0][1]][node]
            cumulative_cost += sub_path_cost
            sub_path = {'from': traversal[node][0][1], 'to': node, 'cost': sub_path_cost}
            path.append(sub_path)
            node = traversal[node][0][1]
        path.reverse()
    return path, cumulative_cost


def uniform_cost_search_or_a_star_based_on_heuristic(origin, destination, heuristic={}):
    nodes_expanded = 0
    nodes_popped = 0
    visited = []
    traversal = {origin: ("\0", 0)}
    cost_sorted_fringe = PriorityQueue()
    cost_sorted_fringe.put((0, origin))
    nodes_generated = 1
    while cost_sorted_fringe.queue:
        node_to_expand = cost_sorted_fringe.get()
        nodes_popped += 1
        if destination == node_to_expand[1]:
            break
        if node_to_expand in visited:
            continue
        visited.append(node_to_expand)
        nodes_generated = expand_node(node_to_expand, cost_sorted_fringe, traversal, nodes_generated, heuristic)
        nodes_expanded += 1
    path, cost = get_cost_and_path_of_traversal(traversal, destination, origin)
    return path, cost, nodes_generated, nodes_expanded, nodes_popped


def get_heuristic_from_file(file):
    heuristic = {}
    file = open(file, 'r')
    while file:
        line = file.readline()
        if "END OF INPUT" in line:
            break
        data = line.split()
        heuristic[data[0]] = int(data[1])
    file.close()
    return heuristic


def get_links_from_file(file):
    generated_links = {}
    file = open(file, 'r')
    while file:
        line = file.readline()
        if "END OF INPUT" in line:
            break
        data = line.split()
        if data[0] in generated_links:
            generated_links[data[0]][data[1]] = int(data[2])
        else:
            generated_links[data[0]] = {data[1]: int(data[2])}
        if data[1] in generated_links:
            generated_links[data[1]][data[0]] = int(data[2])
        else:
            generated_links[data[1]] = {data[0]: int(data[2])}
    file.close()
    return generated_links


links = get_links_from_file(links_file_name)
if len(sys.argv) < 5:
    routes, distance, ng, ne, np = uniform_cost_search_or_a_star_based_on_heuristic(origin=start_state,
                                                                                    destination=goal_state)
else:
    heuristic_file_name = sys.argv[4]
    heuristic_parameters = get_heuristic_from_file(heuristic_file_name)
    routes, distance, ng, ne, np = uniform_cost_search_or_a_star_based_on_heuristic(origin=start_state,
                                                                                    destination=goal_state,
                                                                                    heuristic=heuristic_parameters)
print(f"""Nodes Popped: {np}
Nodes Expanded: {ne}
Nodes Generated: {ng}
Distance: {distance} km""")
print("Route:")
if routes:
    for route in routes:
        print(f"{route['from']} to {route['to']}, {route['cost']:.1f} km")
else:
    print("None")
