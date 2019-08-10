# this script just picks the top n nodes given.

import json
import random

n = 20

# load in data
with open('testgraph2.json') as f:
    graph = json.load(f)

# iterate through first n and save them



keys = list(graph)
degree = len(graph[keys[0]])
nodes = [keys[0]]
min = (keys[0], degree)
i = 1

while i < n:
    degree = len(graph[keys[i]])
    nodes.append(keys[i])
    if degree < min[1]:
        min = (keys[i], degree)
    i += 1
    
while i < len(graph):
    degree = len(graph[keys[i]])
    if degree > min[1]:
        nodes.remove(min[0])
        nodes.append(keys[i])
        min = (keys[i], degree)
        for node in nodes:
            if len(graph[node]) < min[1]:
                min = (node, len(graph[node]))
    i += 1

        


        

# write the chosen nodes 50 times
f = open("submission_high_degree.txt", "w")
submission_str = ''
for node in nodes:
    submission_str += str(node) + '\n'

for i in range(50):
    f.write(submission_str)

f.close()