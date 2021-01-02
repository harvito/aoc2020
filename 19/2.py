with open("input.txt") as f:
  blocks = f.read().split("\n\n")

rulesLines = blocks[0].splitlines()
inputLines = blocks[1].splitlines()

numRules = len(rulesLines)
  
rulesList = [[]] * numRules
referencedBy = [set()] * numRules
memo = [[]] * numRules
activeQueue = []
for line in rulesLines:
  parts = line.split(": ")
  index = int(parts[0])
  ors = parts[1].split(" | ")
  seqs = []
  for seq in ors:
    seqList = seq.split()
    if seqList[0][0] == '"':
      literal = [seqList[0][1]]
      memo[index] = literal
      # print "appending", literal
      seqs.append(literal)
      memo[index] = literal
      activeQueue.append(index)
    else:
      # print "appending", seqList
      seqIntList = [ int(x) for x in seqList ]
      seqs.append(seqList)
      for i in seqIntList:
        referencedBy[i].add(index)
      
      
  rulesList[index] = seqs
  
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
rulesList[8] = [["42"], ["42", "8"]]
rulesList[11] = [["42", "31"], ["42", "11", "31"]]

longestTest = max(len(ele) for ele in inputLines) 

print rulesList
print "base rules:", memo
print "longest test length:", longestTest

rule8count = 0
rule11count = 0
completedSet = set(activeQueue)
i = 0
while len(completedSet) < numRules:
  ruleNo = activeQueue[i]
  rule = rulesList[ruleNo]
  
  # skip if we don't have enough info memoized
  for seq in rule:
    for r in seq:
      if not memo[r]:
        continue
  
  if ruleNo == 8:
    if rule8count > 10:
      completedSet.add(ruleNo)
    else:
      rule8count += 1
  elif ruleNo == 11:
    if rule11count > 10:
      completedSet.add(ruleNo)
    else:
      rule11count += 1
  else:
    completedSet.add(ruleNo)
  
  # find who references this rule
  for r in referencedBy[ruleNo]:
    if (r not in completedSet) or (r in [8, 11]):
      activeQueue.append(r)  
  
  matchesList = [] # should be a list of strings
  for seq in rule:
    
    matching = [""] # another list of matching strings, starting with the empty string
    for rule in seq: # ex 12 71 9
      if not memo[ruleNo]:
        print "UH OH RULE NOT MEMOIZED:", rule
      newMatching = []
      for match in memo[ruleNo]:
        for oldMatch in matching:
          newMatching.append(oldMatch + match)
    
    matchesList += matching # join the rules into 1 string
  memo[ruleNo] = matchesList
  
  i += 1
    
print "OK"