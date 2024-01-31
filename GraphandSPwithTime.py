def addnodes(G,nodes):
    for i in nodes:
        G[i] = []
    return G

def addEdges(G,edges):
    for p in edges:
        G[p[0]] = G[p[0]] + [(p[1],p[2])]
        G[p[1]] = G[p[1]] + [(p[0],p[2])]
    return G

nodes = []
data = []

file = open("locationWithTime.csv", "r") 
for line in file.readlines():
  column=line.split(",")
  x = column[2]
  x = x[:-1]
  p = (column[0],column[1],float(x))
  data.append(p)
  if column[0] not in nodes:
    nodes.append(column[0])
  if column[1] not in nodes:
    nodes.append(column[1])

G = {}
addnodes(G,nodes)
addEdges(G,data)


def Loadgraph(G):
  return G

import math 

def out_edges(G,y):
    pp = []
    x = G[y]
    for p in x:
        pp.append(p)
    return pp

def addNodes(graph,x):
  G ={}
  for i in graph:
    G[i] = x
  return G

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


def sp(graph,s,e):
  PQ=[]
  enqueue(PQ,s,0)
  Dist=addNodes(graph,math.inf)
  Dist[s]=0
  visited = set()

  Prev=addNodes(graph, None)

  while len(PQ)>0:
    u=PQ.pop(0)
    children=out_edges(graph,u[0])

    for child,weight in children:
      if child in visited:
        continue
      alt=Dist[u[0]]+weight
      if alt<Dist[child]:
        Dist[child]=alt
        Prev[child]=u[0]
        enqueue(PQ,child,alt)
    visited.add(u[0])
  path=[]
  x=e
  #return Prev
  while x!=None:
      path.append(x)
      x=Prev[x] 
  path.reverse()
  
  return path,Dist[e]
