# this script picks from nodes with high closeness centrality

import json
import random
import networkx as nx
import operator
import math

n = 20

# load in data
with open('8.20.2.json') as f:
    graph = json.load(f)

# iterate through first n and save them

keys = graph.keys()
G = nx.Graph()

for item in graph.items():
	for j in range(len(item[1])):
		G.add_edge(item[0], item[1][j])

closeness = nx.closeness_centrality(G)

node_closeness = []

for point in closeness.keys():
	# use a list so that we can update based on other measures.
	node_closeness.append([point, closeness[point]])

node_closeness = sorted(node_closeness, key=operator.itemgetter(1))[::-1]
top_closeness = []

# Find the top 2 * n nodes based off of closeness
for i in range(2*n):
	top_closeness.append(node_closeness[i])

# Of these top 2n, take the n with the highest 
# clustering coefficient
clustering = nx.clustering(G)
for point in top_closeness:
	point[1] *= 2
	point[1] += clustering[point[0]]
top_closeness = sorted(top_closeness, key=operator.itemgetter(1))[::-1]

top_nodes = []
for i in range(n):
	top_nodes.append(top_closeness[i][0])



# write the chosen nodes 50 times
f = open("closeness_clustering_submission.txt", "w")
submission_str = ''
for node in top_nodes:
    submission_str += str(node) + '\n'

for i in range(50):
    f.write(submission_str)

f.close()