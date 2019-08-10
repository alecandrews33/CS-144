import json
import networkx as nx
import operator

# number of nodes that are submitted
n = 35

# number considered of top degree nodes
num_considered = n * 3

with open('8.35.2.json') as f:
    graph = json.load(f)

keys = graph.keys()
G = nx.Graph()

for item in graph.items():
    for j in range(len(item[1])):
        G.add_edge(item[0], item[1][j])

# get high degree corresponding to top ppl * number of nodes
degree = len(graph[keys[0]])
high_degree_nodes = [keys[0]]
min = (keys[0], degree)
i = 1

while i < num_considered:
    degree = len(graph[keys[i]])
    high_degree_nodes.append(keys[i])
    if degree < min[1]:
        min = (keys[i], degree)
    i += 1
    
while i < len(graph):
    degree = len(graph[keys[i]])
    if degree > min[1]:
        high_degree_nodes.remove(min[0])
        high_degree_nodes.append(keys[i])
        min = (keys[i], degree)
        for node in high_degree_nodes:
            if len(graph[node]) < min[1]:
                min = (node, len(graph[node]))
    i += 1

# get the top n closeness nodes from these nodes
node_closeness = []
for node in high_degree_nodes:
    c = nx.closeness_centrality(G, node)
    node_closeness.append((node, c))

top_node = max(node_closeness, key = operator.itemgetter(1))

top_neighbor_degrees = []
neighbors = list(G[top_node[0]])
for node in neighbors:
    degree = len(G[node])
    top_neighbor_degrees.append((node, degree))

top_neighbor_degrees = sorted(top_neighbor_degrees, key = operator.itemgetter(1))[::-1]

if len(top_neighbor_degrees) > num_considered:
    top_neighbor_degrees = top_neighbor_degrees[:num_considered]

top_neighbors = []
for node in top_neighbor_degrees:
    close = nx.closeness_centrality(G, node[0])
    top_neighbors.append((node[0], close))

top_nodes = sorted(top_neighbors ,key=operator.itemgetter(1))[::-1]
top_nodes = top_nodes[:n]


    
# write the chosen nodes 50 times
f = open("closeness_gang_up_submission.txt", "w")
submission_str = ''
for node in top_nodes:
    submission_str += str(node[0]) + '\n'

for i in range(50):
    f.write(submission_str)

f.close()

