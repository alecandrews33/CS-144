#!/usr/bin/env python

import sys

for line in sys.stdin:
    # grab different components
    prefix, value = line.split('\t')

    # grab the node_id from the prefix
    node_id = prefix[7:]
    
    if node_id == 'list':
        adj_str = node_id + '\t' + value
        
    else:
        # get the adjacency row
        adjacency_row = value.strip().split(',')

        # set the old rank to the new rank
        adjacency_row[1] = adjacency_row[0]

        # get the numeric value of the rank
        rank = float(adjacency_row[0])

        # if it has no neighbors, it contributes "1" to itself
        if len(adjacency_row) == 2:
            sys.stdout.write(node_id + '\t' + str(rank) + '\n')

        # otherwise, emit the contribution to each neighbor
        else:
            neighbors = adjacency_row[2:]
            contribution = rank / float(len(neighbors))
            if contribution > 0.001:
                for n in neighbors:
                    sys.stdout.write(n + '\t' + str(contribution) + '\n')

        # lastly, output the adjacency row with a | in front
        adj_str = node_id + '\t|'
        for i in adjacency_row:
            adj_str += i + ','

        adj_str = adj_str[:-1] + '\n'

    sys.stdout.write(adj_str)

























































# # Split the line on the tab and grab id and the list that follows.
# l = line.strip().split("\t")
# node_id = l[0][7:]
# adjacency_row = l[1].split(",")
# adjacency_row[0] = float(adjacency_row[0])

# # Calculate the node's current rank
# rank = adjacency_row[0]

# # Update the old rank
# adjacency_row[1] = adjacency_row[0]

# # recreate the adjacency row, but with a | at the start so we know it's
# # an adjacency row
# adj_row_str = '|'
# for i in range(len(adjacency_row)):
#     adj_row_str += str(adjacency_row[i]) + ','
# # take out last comma
# adj_row_str = adj_row_str[:-1]

# # If there are neighbors, grab them, and the node's contribution to them 
# if len(adjacency_row) > 2:
#     neighbors = adjacency_row[2:]
#     contribution = rank / float(len(neighbors))

#     # print out the contribution for each neighbor
#     for node in neighbors:
#         sys.stdout.write("%s\t%f" % (node, contribution) + "\n")

# else:
#     # it will only contribute to itself
#     neighbors = []
#     sys.stdout.write("%s\t%f" % (node_id, rank) + "\n")


# # output the special adj row string
# sys.stdout.write("%s\t%s" % (node_id, adj_row_str) + "\n")

