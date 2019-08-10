# this script picks from nodes with high clustering coefficients

import json
import random
import networkx as nx
import operator

n = 5

# load in data
with open('testgraph1.json') as f:
    graph = json.load(f)

# iterate through first n and save them

keys = graph.keys()
G = nx.Graph()

for item in graph.items():
	for j in range(len(item[1])):
		G.add_edge(item[0], item[1][j])

clusters = nx.clustering(G)

node_clustering = []
min_cluster = 0

for point in clusters.keys():
	# the edges are tuples - this must be fixed
	node_clustering.append((point, clusters[point], list(G[point])))

node_clustering = sorted(node_clustering, key=operator.itemgetter(1))[::-1]
top_nodes = []

for i in range(n):
	top_nodes.append(node_clustering[i][0])

# write the chosen nodes 50 times
f = open("top_clustering_submission.txt", "w")
submission_str = ''
for node in top_nodes:
    submission_str += str(node) + '\n'

for i in range(50):
    f.write(submission_str)

f.close()