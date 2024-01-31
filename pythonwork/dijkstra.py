def AddVertex(graph, label):
  
  if label not in graph:
    graph[label] = []
  return graph

# Delete the vertex source the graph having the same label as provided
def DeleteVertex(graph, label):
  del(graph[label])
  for i in graph:
    for j in graph[i]:
        if j[0] == label:
            graph[i].remove(j)
  return graph

# Delete vertices source the graph for the given labels
def DeleteVertices(graph, labels):
  # labels: a list
  for node in labels:
    del(graph[i])
    for i in graph:
            for j in graph[i]:
                if j[0] == node:
                    graph[i].remove(j)
    return graph
  

# For the following functions, do not add/delete an edge if any vertex involved in the edge does not exist.

# Add an edge in the graph
def AddEdge(graph, source, target, directed):
  # source: label to identify the source vertex
  # target: lbael to identify the target vertex
  # directed: whether the edge is directed or undirected
  if source in graph  and target in graph:
    graph[source] = graph[source] + [target]
    if directed == False:
      graph[target] = graph[target] + [source]

# Add an edge in the graph with a weight
def AddWeightedEdge(graph, source, target, weight, directed):
  # source: label to identify the source vertex
  # target: label to identify the target vertex
  # weight: the weight of the edge
  # directed: whether the edge is directed or undirected
  if source in graph and target in graph:
    graph[source] = graph[source] + [(target,weight)]
    if directed == False:
      graph[target] = graph[target] + [(source,weight)]
  return 

def LoadGraph(fileName, weighted = True, directed = False):
  # weighted = True if the edge list contains weight
  # directed = True if the given edge list is for directed graph
  file  = open(fileName,"r")
  data = []
  graph = {}
  for line in file.readlines():
    data.append(line)
    
  cities = []
  connectedcity_time = []

  for i in range(len(data)):
    data[i] = data[i].strip().split(",")
    if data[i][0] not in cities:
      cities.append(data[i][0])
    graph[data[i][0]] = []
    connectedcity_time.append((data[i][1],int(data[i][2])))
    
    
  print(graph)
  
  
LoadGraph("main file for project.csv", weighted = True, directed = False)

  # for i in data[1:]:
  #   lst = i.split()
  #   print(lst)
  #   if weighted == True:
  #     AddWeightedEdge(graph,lst[0],lst[1],(lst[2]),directed=False)
  #   if weighted == False:
  #     AddEdge(graph,lst[0],lst[1],directed=False)
  #   if lst[0] not in graph:
  #     AddVertex(graph,lst[0])
  #   if lst[1] not in graph:
  #     AddVertex(graph,lst[1])
  # return graph

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

#print(LoadGraph("main file for project.csv", True, False))