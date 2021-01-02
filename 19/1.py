with open("input.txt") as f:
  blocks = f.read().split("\n\n")
  
  
rulesDict = {}
for line in blocks[0].splitlines():
  parts = line.split(": ")
  index = parts[0]
  ors = parts[1].split(" | ")
  seqs = []
  for seq in ors:
    seqList = seq.split()
    if seqList[0][0] == '"':
      literal = [seqList[0][1]]
      # print "appending", literal
      seqs.append(literal)
    else:
      # print "appending", seqList
      seqs.append(seqList)
  rulesDict[index] = seqs
  
# returns a list of all the strings 
# if the rule is an or, return a list of the possibilities
# if the rule is a sequence, return again a list of the possibilities
def makePossibilities(ruleNo):
  # print ruleNo, rulesDict[ruleNo]
  matchesList = [] # should be a list of strings
  for seq in rulesDict[ruleNo]:
    matching = [""] # another list of matching strings, starting with the empty string
    for rule in seq: # ex 12 71 9
      if rule in "ab": # base case
        # print "HIT:", rule
        for i in range(len(matching)):
          matching[i] += rule
      else:
        newMatching = []
        for possibility in makePossibilities(rule):
          for match in matching:
            newMatching.append(match + possibility)
        matching = newMatching
    
    matchesList += matching # join the rules into 1 string
  return matchesList
  
allMatchingSequences = makePossibilities("0")
for matches in allMatchingSequences:
  pass # print matches
print len(allMatchingSequences)

count = 0
for line in blocks[1].splitlines():
  if line in allMatchingSequences:
    count += 1
print count