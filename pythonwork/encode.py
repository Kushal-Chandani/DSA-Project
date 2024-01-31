# # prompt the user to enter a string
# # encode it using shaSum
# # print the string


# string = input("Enter a string: ")
# import hashlib
# print(hashlib.sha256(string.encode()).hexdigest())

import csv

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G


def addEdges(G, edge_list, directed=False):
    if directed == True:
        for i in edge_list:
            G[i[0]].append((i[1], i[2]))
        return G
    elif directed == False:
        for y in edge_list:
            G[y[1]].append((y[0], y[2]))
        for x in edge_list:
            G[x[0]].append((x[1], x[2]))
        return G

Graph = {}
edges = []
nodes = []

with open('locations.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        edges.append((row['from'], row['to'], float(row["time"])))
        nodes.append(row["from"])

    nodes = list(dict.fromkeys(nodes))

Graph = addNodes(Graph, nodes)
Graph = addEdges(Graph, edges, directed=True)
print(Graph)

import math

def addNodes(g,value):
  graph = {}
  for i in g:
    graph[i] = value

  return graph

def enqueue(queue,node,value):
  check = False
  for i in range(len(queue)):
    if queue[i][0] == node:
      if queue[i][1] > value:
        queue[i] = (node,value)
        check = True
        break
  if check == False:
    queue.append((node,value))
  queue.sort(key = lambda x: x[1])

def out_edges(g,u):
  return g[u]

def dequeue(q):
  return q.pop(0)

def getShortestPath(graph,s,end):
  pq = []
  enqueue(pq,s,0)

  dist = addNodes(graph,math.inf)
  dist[s] = 0

  Prev = addNodes(graph,None)

  while len(pq)> 0:
    
    u = dequeue(pq)
     
    children = out_edges(graph,u[0])

    for child,weight in children:
      alt = dist[u[0]] + weight
      if alt< dist[child]:
        dist[child ] = alt
        Prev [child] = u[0]
        enqueue(pq,child,alt)

  
  path=[]
  x=end
  
  while x!=None:
      path.append(x)
      x=Prev[x] 
  path.reverse()
  new = []

  for i in range(len(path)):
    if path[i]!= end:
      new+=[(path[i],path[i+1])]

  return new