# this script generates several test graphs using networkx
import json
import random
import networkx as nx
from networkx.readwrite import json_graph

graphs = {
    # ERDOS RENYI 0.2
    'gnp_1500_2' : nx.fast_gnp_random_graph(1500, 0.2), \
    'gnp_2000_2' : nx.fast_gnp_random_graph(2000, 0.2), \
    'gnp_2500_2' : nx.fast_gnp_random_graph(2500, 0.2), \

    # ERDOS RENYI 0.5
    'gnp_1500_5' : nx.fast_gnp_random_graph(1500, 0.5), \
    'gnp_2000_5' : nx.fast_gnp_random_graph(2000, 0.5), \
    'gnp_2500_5' : nx.fast_gnp_random_graph(2500, 0.5), \

    # ERDOS RENYI 0.7
    'gnp_1500_7' : nx.fast_gnp_random_graph(1500, 0.7), \
    'gnp_2000_7' : nx.fast_gnp_random_graph(2000, 0.7), \
    'gnp_2500_7' : nx.fast_gnp_random_graph(2500, 0.7), \


    # Regular graphs (all nodes have equal degrees)
    'reg_500_20' : nx.random_regular_graph(20, 500), \
    'reg_1000_20' : nx.random_regular_graph(20, 1000), \
    'reg_1500_20' : nx.random_regular_graph(20, 1500), \
    'reg_2000_20' : nx.random_regular_graph(20, 2000), \
    'reg_2500_20' : nx.random_regular_graph(20, 2500), \

    # lobster graphs (a caterpillar with branches)
    'lob_500_5_5' : nx.random_lobster(500, 0.5, 0.5), \
    'lob_1000_5_5' : nx.random_lobster(1000, 0.5, 0.5), \
    'lob_1500_5_5' : nx.random_lobster(1500, 0.5, 0.5), \
    'lob_2000_5_5' : nx.random_lobster(2000, 0.5, 0.5), \
    'lob_2500_5_5' : nx.random_lobster(2500, 0.5, 0.5), \

    # newman_watts_strogatz_graph
    'nws_500_25_3' : nx.newman_watts_strogatz_graph(500, 25, 0.3), \
    'nws_1000_25_3' : nx.newman_watts_strogatz_graph(1000, 25, 0.3), \
    'nws_1500_25_3' : nx.newman_watts_strogatz_graph(1500, 25, 0.3), \
    'nws_2000_25_3' : nx.newman_watts_strogatz_graph(2000, 25, 0.3), \
    'nws_2500_25_3' : nx.newman_watts_strogatz_graph(2500, 25, 0.3), \

    'nws_500_25_66' : nx.newman_watts_strogatz_graph(500, 25, 0.66), \
    'nws_1000_25_66' : nx.newman_watts_strogatz_graph(1000, 25, 0.66), \
    'nws_1500_25_66' : nx.newman_watts_strogatz_graph(1500, 25, 0.66), \
    'nws_2000_25_66' : nx.newman_watts_strogatz_graph(2000, 25, 0.66), \
    'nws_2500_25_66' : nx.newman_watts_strogatz_graph(2500, 25, 0.66)
}

# create a test_graph for each
for key in graphs.keys():
    features = key.split('_')
    graph_name = features[0]
    num_nodes = features[1]

    filename = 'test_graphs/test_graph_'+graph_name+'_'+num_nodes

    # generate the filename
    if graph_name == 'gnp':
        prob = features[2]
        prob = '0.' + prob

        filename +='_'+prob+'.json'

    elif graph_name == 'reg':
        degree = features[2]
        filename += '_'+degree+'.json'

    elif graph_name == 'lob':
        prob1 = features[2]
        prob1 = '0.' + prob1
        prob2 = features[3]
        prob2 = '0.' + prob2
        filename +='_'+prob1+'_'+prob2+'.json'

    elif graph_name == 'nws':
        intervals = features[2]
        prob = features[3]
        prob = '0.' + prob
        filename +='_'+intervals+'_'+prob+'.json'

    # create/erase the file
    f = open(filename, "w")
    f.write('')
    f.close()

    # write to file
    data = nx.to_dict_of_lists(graphs[key])
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

    print("Generated graph: " + filename)







