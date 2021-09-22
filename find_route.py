# This is a python application to implement the following tree search algorithms:
#
# 1. Informed Search using A* Search Algorithm
# 2. Uninformed Search using uniform cost search algorithm
import sys
from queue import PriorityQueue

# Getting the required arguments:
# <LINK_FILE_NAME> file where the link is stored, it does accept the path where the file is stored
# with respect to the current location where the program is running.
# <START_STATE> which is the start node at which the search has to start.
# <GOAL_STATE> which is the destination node at which the search has to end.
links_file_name = sys.argv[1]
start_state = sys.argv[2]
goal_state = sys.argv[3]


# Successor Function: Function to expand any given node and generate the successors.
# Based on heuristic it adds the cost of how far away it is from the source to the fringe for an informed search.
# If the heuristic is given it does an A* search else does an uniform cost search algorithm.
# It stores the information of the traversed path with cost as a
# tuple (<NODE_NAME>, <CUMULATIVE_COST_TO_GET_TO_THE_NODE>)
# Also it counts and returns the number of nodes generated.
def expand_node(node_to_expand, fringe, traversal, total_generated, heuristic):
    generated = total_generated
    for link in links[node_to_expand[1]]:
        cumulative_cost = links[node_to_expand[1]][link] + traversal[node_to_expand[1]][1]
        # This is where the programme runs as a informed or uninformed search based on the heuristic.
        # If the heuristic is given we add it to the cumulative cost before appending to the fringe.
        # Else we just append it with the cumulative cost.
        # Which will be latter used by our algorithm to decide on the next priority expanding node.
        fringe.put((cumulative_cost + heuristic[link] if heuristic else cumulative_cost, link))
        generated += 1
        if link not in traversal:
            traversal[link] = (node_to_expand, cumulative_cost)
    return generated


# This function is used to get the total cumulative cost for traversal of the route to get from start state to the
# goal state.
# It returns the path taken and the cumulative cost.
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


# This is the function which performs graph search based on the fringe. We use a Priority queue ordered based on the
# cost of getting to a node.
def uniform_cost_search_or_a_star_based_on_heuristic(origin, destination, heuristic=None):
    if heuristic is None:
        heuristic = {}
    nodes_expanded = 0
    nodes_popped = 0
    visited = []
    traversal = {origin: ("\0", 0)}
    cost_sorted_fringe = PriorityQueue()
    # To store the values in the fringe based on the cost in the tuple format (<COST>, <NODE_NAME>). The Priority
    # Queue handle the order based on the least COST in the front of the queue.
    cost_sorted_fringe.put((0, origin))
    nodes_generated = 1
    # We end the iteration if the fringe gets empty
    while cost_sorted_fringe.queue:
        # To pop the least cost element out of the queue which will be there at the front of the queue
        node_to_expand = cost_sorted_fringe.get()
        nodes_popped += 1
        # We end the loop if we have reached our destination
        if destination == node_to_expand[1]:
            break
        # If the node is already visited we have popped it out of the fringe earlier and we just continue the iteration
        if node_to_expand in visited:
            continue
        # We now expand the node based on heuristic value as explained before and add the children to the fringe
        nodes_generated = expand_node(node_to_expand, cost_sorted_fringe, traversal, nodes_generated, heuristic)
        nodes_expanded += 1
        # Since we have expanded the node we took out of the fringe we add it to the visited list
        visited.append(node_to_expand)
    # Now we calculate the cumulative cost and route to take to get from the start state to the goal state.
    path, cost = get_cost_and_path_of_traversal(traversal, destination, origin)
    return path, cost, nodes_generated, nodes_expanded, nodes_popped


# This is the function used to parse the data from the Heuristic file.
def get_heuristic_from_file(file):
    heuristic = {}
    file = open(file, 'r')
    while file:
        line = file.readline()
        # We run the loop line by line till we reach the "END OF INPUT" line
        if "END OF INPUT" in line:
            break
        data = line.split()
        heuristic[data[0]] = int(data[1])
    file.close()
    return heuristic


# This is the function used to parse the data from the Links file.
def get_links_from_file(file):
    generated_links = {}
    file = open(file, 'r')
    while file:
        line = file.readline()
        # We run the loop line by line till we reach the "END OF INPUT" line
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


# We first get the links from the links file
links = get_links_from_file(links_file_name)

# Based on the number of arguments we will check if we need to do informed/uninformed search algorithm
if len(sys.argv) < 5:
    # If there are 4 argument we do uninformed search using the uniform cost search algorithm for that we don't need
    # the heuristic file
    routes, distance, ng, ne, np = uniform_cost_search_or_a_star_based_on_heuristic(origin=start_state,
                                                                                    destination=goal_state)
else:
    # If there are more than 4 arguments then we parse the data from the heuristic file and pass it on to our algorithm
    heuristic_file_name = sys.argv[4]
    heuristic_parameters = get_heuristic_from_file(heuristic_file_name)
    routes, distance, ng, ne, np = uniform_cost_search_or_a_star_based_on_heuristic(origin=start_state,
                                                                                    destination=goal_state,
                                                                                    heuristic=heuristic_parameters)
# Our algorithm returns the path taken, distance/cumulative cost, number of nodes generated, number of nodes
# expanded, number of nodes popped which we will display as an output in the console
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
