# Assignment1
# Uninformed search and Informed search
# Name : Sushmitha Nagarajan
# ID : 1001556348

from sys import argv

script,filename,source,destination,type = argv
#Construct a dictionary for graph tree ,graph cost
Graph_tree = {}
Graph_cost = {}
heuristic = open(filename, 'r')
# Take the lines in the heuristic file and convert them into dictionary
for line in heuristic:
    values = line.split()
    if values[0] in Graph_tree:
        Graph_tree[values[0]].append(values[1])
    else:
        Graph_tree[values[0]] = [values[1]]
print(Graph_tree)


# Node create at every place where the graph grows dynamically
def node():
    Graph_cost = []
    heuristic = open(filename, 'r')
    for line in heuristic:
        values = line.split()
        src = values[0]
        dest = values[1]
        cost = values[2]
        Graph_cost.append((src, dest, cost))
    print(Graph_cost)
    return Graph_cost


# find the neighbours of every node in the source to destination
def find_neighbours(from_place, to_place):
    if from_place == to_place:
        return "There is no routes between these two places"
    if from_place not in Graph_tree.keys():
        return "There is no such distance"
    if from_place in Graph_tree.keys():
        print(Graph_tree[from_place])
        return Graph_tree[from_place]


# find the cost from source to destination for every fringe
def find_cost(from_place, to_place):
    get_neighbours = find_neighbours(from_place)
    # initial_path_cost = 0
    path_cost = 0
    visited = []
    while True:
        if get_neighbours == to_place:
            search(from_place)
            visited.append(get_neighbours)
            for get_neighbour in Graph_cost:
                print("distance: "+path_cost+" kms\nroute:"+visited)
                return path_cost
        elif get_neighbours in Graph_cost:
            visited.append(get_neighbours)
            for depth_node in get_neighbours:
                find_neighbours(depth_node)
				print("distance: "+path_cost+" kms\nroute:"+visited)
                return find_neighbours()


# defines the queue and vertices from every node
def __init__(self, graph):
    self.graph = graph
    self.queue = []
    node()

# add edges dynamically with next set of fringes
def add(self, node):
    self.queue.append(node)
    self.queue.sort(key=lambda node: node.pathCost)
    nodes = node()

# search for the nearest neighbours that are connected to source
def search(neighbours):
    find_neighbours(neighbours)
    paths = find_neighbours(neighbours)
    for path in paths:
        if paths in path.source:
            paths.append(path)
    for path in paths:
        paths.remove(path)
    return paths


# Invokes the program by checking if the search is uninformed or informed
if type == "uninf":
    find_cost(source, destination, path=1)
else:
    find_cost(source, destination,path=0)