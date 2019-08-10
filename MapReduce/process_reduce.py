#!/usr/bin/env python

import sys
from operator import itemgetter

#
# This program simply represents the identity function.
#



rows = []
rowsNumbers = []


top50_new = []
top50_old = []
mintuple_new = []

for line in sys.stdin:
    adjacency_row = []

    # split string input
    node_id, value = line.split("\t")

    if node_id != "list":
        # split into list
        value_list = value.strip().split(',')

        # Initialize neighbors string
        neighbors = ''

        # make list of values floats
        for i in range(len(value_list)):
            if i <= 1:
                adjacency_row.append(float(value_list[i]))
            else:
                neighbors += ',' + str(value_list[i])
        

        # get ranks
        new = adjacency_row[0]
        old = adjacency_row[1]

        # make row for sorting/finding top 20
        rowI = [node_id, new]


        if len(top50_new) < 50:
            top50_new.append(rowI)

            # initialize the mintuples
            if mintuple_new == []:
                mintuple_new = rowI

            else:
                # set new mintuples if the new value is smaller
                if mintuple_new[1] > rowI[1]:
                    mintuple_new = rowI

        else:
            if mintuple_new[1] < rowI[1]:
                top50_new.remove(mintuple_new)
                top50_new.append(rowI)
                mintuple_new = rowI

                # get new min
                for j in top50_new:
                    if j[1] < mintuple_new[1]:
                        mintuple_new = j


        # keep track in case we need to keep going
        final_row = 'NodeId:' + node_id + '\t' + \
                                str(new) + ',' + str(old) + neighbors
                                

        # for printing
        rows.append(final_row)
        rowsNumbers.append(rowI)
    # Catch the case where we get the artificial node
    else:
        top50_old = value.strip('\n').split(",")

converged = False

if top50_old != []:
    top50_new = sorted(top50_new, key=itemgetter(1))[::-1]
    converged = True
    for i in range(len(top50_new)):
        if top50_new[i][0] != top50_old[i]:
            converged = False

# once we read in all the output, determine if we stop
if converged:
    for i in range(20):
        sys.stdout.write("FinalRank:" + str(top50_new[i][1]) + '\t' + \
                            str(top50_new[i][0]) + '\n')

else:
    old_list = ""
    for node in top50_new:
        old_list += str(node[0]) + ","
    old_list = old_list[:-1]
    rows.append('NodeId:list' + '\t' + old_list)
    # output so we can restart
    for line in rows:
        sys.stdout.write(line + '\n')