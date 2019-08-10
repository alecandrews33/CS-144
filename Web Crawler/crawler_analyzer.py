from fetcher3 import *
import networkx as nx
import time
import json
import matplotlib.pyplot as plt
import numpy as np

def load_dicts():
	with open("hyperlinks.txt", "r") as f1:
		links = json.load(f1)
	with open("hyperlinks_to.txt", "r") as f2:
		links_to = json.load(f2)
	return links, links_to

if __name__ == "__main__":
	links, links_to = load_dicts()
	G = nx.Graph()

	for x in links.keys():
		for y in links[x]:
			if "caltech.edu" not in y:
				links[x].remove(y)

	links_nodes = list(links.keys())
	links_to_nodes = list(links_to.keys())
	for x in links_to_nodes:
		if "caltech.edu" not in x:
			links_to.pop(x)
	links_to_nodes = list(links_to.keys())


	node_set = set(links_nodes).union(set(links_to_nodes))
	G.add_nodes_from(list(node_set))
	for node in links_nodes:
		G.add_edges_from([(node, x) for x in links[node]])

	links_degrees = []
	for node in links_nodes:
		links_degrees.append(len(links[node]))
	links_degrees = sorted(links_degrees)

	links_to_degrees = []
	for node in links_to_nodes:
		links_to_degrees.append(len(links_to[node]))
	links_to_degrees = sorted(links_to_degrees)

	avg_cluster = nx.average_clustering(G)
	overall_cluster = nx.transitivity(G) * 3
	print(avg_cluster)
	print(overall_cluster)
	max_diam = nx.diameter(G)
	avg_diam = nx.average_shortest_path_length(G)
	print(max_diam)
	print(avg_diam)
	



	plt.figure()
	values1, base1 = np.histogram(links_degrees, bins = 'auto')
	ccdf = np.ones(len(values1)) - np.cumsum(values1 / sum(values1))
	plt.plot(ccdf)
	plt.title("CCDF of Hyperlinks Per Page")
	plt.xlabel("Number of Hyperlinks")
	plt.ylabel("Percentage of Pages")
	plt.show()
	plt.close()

	plt.figure()
	values2, base2 = np.histogram(links_to_degrees, bins = 'auto')
	ccdf = np.ones(len(values2)) - np.cumsum(values2 / sum(values2))
	plt.plot(ccdf)
	plt.title("CCDF of Hyperlinks To Each Page")
	plt.xlabel("Number of Hyperlinks To Page")
	plt.ylabel("Percentage of Pages")
	plt.show()
	plt.close()

	plt.figure()
	plt.hist(links_degrees, bins = 200, color = 'blue')
	plt.title("Links Per Page")
	plt.xlabel("Degree of Nodes")
	plt.ylabel("Number of Nodes")
	plt.show()
	plt.close()

	plt.figure()
	plt.hist(links_to_degrees, bins = 200, color = 'blue')
	plt.title("Links To Each Page")
	plt.xlabel("Degree of Nodes")
	plt.ylabel("Number of Nodes")
	plt.show()
	