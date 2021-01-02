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
    
    
# count paths to dest, bfs
def countPaths(graph, destNode):
  setOfContaining = set()
  currentNodeSet = {destNode}
  while len(currentNodeSet) > 0:
    snapshot = currentNodeSet
    print currentNodeSet
    toAdd = set()
    for n in snapshot:
      for edge in graph:
        if edge.dest == n:
          if edge.src not in setOfContaining:
            setOfContaining.add(edge.src)
            toAdd.add(edge.src)
    currentNodeSet = toAdd
  return len(setOfContaining)
      
        

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