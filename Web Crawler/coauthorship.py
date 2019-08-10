import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

NUM_NODES = 4158

if __name__ == "__main__":
	G = nx.Graph()
	with open("gr_qc_coauthorships.txt", "r") as f:
		for line in f:
			lst = line.strip('\n').split(' ')
			G.add_node(lst[0])
			G.add_node(lst[1])
			G.add_edge(lst[0], lst[1])
	degrees = []
	for node in G.nodes():
		degrees.append(G.degree(node))
	degrees = sorted(degrees)
	avg_cluster = nx.average_clustering(G)
	overall_cluster = nx.transitivity(G) * 3
	'''max_diam = nx.diameter(G)
	avg_diam = nx.average_shortest_path_length(G)
	print("Average clustering coefficient is: " + str(avg_cluster))
	print("Overall clustering coefficient is: " + str(overall_cluster))
	print("Maximal diameter is: " + str(max_diam))
	print("Average diameter is: " + str(avg_diam))
	plt.hist(degrees, bins = 'auto')
	plt.xlabel("Degree of node")
	plt.ylabel("Number of nodes")'''
	plt.figure()
	values, base = np.histogram(degrees, bins = 40)
	ccdf = np.ones(len(values)) - np.cumsum(values / sum(values))
	plt.plot(ccdf)
	plt.title("CCDF of Degree Nodes")
	plt.xlabel("Degree of Node")
	plt.ylabel("Probability of Degree")
	plt.show()
	

	