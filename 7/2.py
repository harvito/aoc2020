# data structure to store graph edges
class Edge:
  def __init__(self, src, dest, weight):
    self.src = src
    self.dest = dest
    self.weight = weight
    
# print adjacency list representation of graph
def printGraph(graph):
  for edge in graph:
    # print current vertex and all its neighboring vertices
    print "(", edge.src, "->", edge.dest, ")", edge.weight
    
    
# count paths from src, dfs
def countPaths(graph, srcNode):
  count = 0
  currentNodeList = [srcNode]
  while len(currentNodeList) > 0:
    snapshot = currentNodeList
    print count, currentNodeList
    toAdd = []
    for n in snapshot:
      for edge in graph:
        if edge.src == n:
          count += edge.weight
          for i in range(edge.weight):
            toAdd.append(edge.dest)
    print toAdd
    currentNodeList = toAdd
  return count
      
        

with open('input.txt') as f:
  lines = f.read().splitlines()
  
edgeList = []
  
for line in lines:
  # print line
  words = line.split()
  srcNode = words[0] + words[1]
  if words[4] == "no": # leaf
    print srcNode, "is a leaf"
  else:
    for i in range(4, len(words), 4):
      # print words[i] + words[i+1] + words[i+2] + words[i+3]
      weight = int(words[i])
      destNode = words[i+1] + words[i+2]
      edgeList.append(Edge(srcNode, destNode, weight))
     

      
print countPaths(edgeList, "shinygold")
# mySet = {"hello"}
# print mySet

# 183 too high
# not 15
# 178 too high