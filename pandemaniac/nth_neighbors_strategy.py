# this script just picks the first n nodes given.
import json
import random
import bisect as b

# number of seeds
n = 5

# finds number of unique values that exist in node compared to seen
def compareUniques(d, seen, node):
    values = d[node]

    uniqueVals = []

    for x in values:
        if x not in seen:
            uniqueVals.append(x)

    return (len(uniqueVals), uniqueVals)

# goes through the nodes
# returns (the node corresponding to the most unique values, 
#           the new seen array)
def findMostUniques(d, seen, nodes, nodesPicked):
    maxvalue = -1
    bestNode = None
    bestUniqueVals = None
    for node in nodes:
        if node in nodesPicked:
            break

        amount, uniqueVals = compareUniques(d, seen, node)
        if amount > maxvalue:
            maxvalue = amount
            bestNode = node
            bestUniqueVals = uniqueVals

    if bestUniqueVals != None:
        newSeen = seen + bestUniqueVals
    else:
        newSeen = seen

    return (bestNode, newSeen)

def getBestNodeNotSeen(nodes, nodesPicked):
    for node in nodes[::-1]:
        print(node)
        if node not in nodesPicked:
            return node

    return None

def main():
    # number of iterations deep we check
    iterations = 1

    # load in data
    with open('testgraph2.json') as f:
        graph = json.load(f)

    # iterate through all nodes and find how many nodes they could infect
    # in x iterations

    keys = graph.keys()
    totalNodes = len(keys)

    print("Total nodes: " + str(len(keys)))

    ranking = []
    counts_ranking = []
    counts = {}
    seen_sets = {}
    queue1 = []
    queue2 = []

    # for every key
    for key in keys:
        # keep track of number of infected keys
        count = 0
        seen_sets[key] = set([key])

        queue1 = graph[key]
        queue2 = []

        # go "iterations" amount deep
        for i in range(iterations):

            # alternate between adding to queue1 or queue2
            # add all the children we want to explore and count them as infected
            if i % 2 == 0:
                queue2 = []
                for subkey in queue1:
                    count += len(graph[subkey])
                    seen_sets[key].update(graph[subkey])
                    for value in graph[subkey]:
                        queue2.append(value)

            else:
                queue1 = []
                for subkey in queue2:
                    count += len(graph[subkey])
                    seen_sets[key].update(graph[subkey])
                    for value in graph[subkey]:
                        queue1.append(value)

        # save the count for each key
        counts[key] = count

        # insert into sorted array
        crIndex = b.bisect_left(counts_ranking, count)
        counts_ranking.insert(crIndex, count)

        # insert into keys sorted array
        ranking.insert(crIndex, key)

    # we should now try to maximize how many we pick such that we get the most
    # amount of unique nodes
    start_node = ranking[-1]
    seen = list(seen_sets[start_node])
    best_nodes = [start_node]
    for i in range(2,n+1):
        new_node, seen = findMostUniques(seen_sets, seen, keys, best_nodes)
        print(len(seen))

        if new_node == None:
            new_node = getBestNodeNotSeen(keys, best_nodes)
        best_nodes.append(new_node)

    print("best nodes are: " + str(best_nodes))
    print("unique nodes to be seen: " + str(len(seen)))

    # write the chosen nodes 50 times
    f = open("submission_neighbors.txt", "w")
    submission_str = ''
    for node in best_nodes:
        submission_str += str(node) + '\n'

    for i in range(50):
        f.write(submission_str)

    f.close()

main()