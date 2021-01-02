with open("input.txt") as f:
  blocks = f.read().split("\n\n")

def parseRules(block):
  lines = block.splitlines()
  rules = []
  for line in lines:
    split1 = line.split(": ")
    field = split1[0]
    ranges = split1[1].split(" or ")
    parsedRanges = []
    for range in ranges:
      bounds = range.split("-")
      lowerBound = int(bounds[0])
      upperBound = int(bounds[1])
      parsedRanges.append((lowerBound, upperBound))
    rules.append((field, parsedRanges))
  return rules
  
def satisfiesARule(rules, v):
  for field, ranges in rules:
    for range in ranges:
      if range[0] <= v <= range[1]:
        return True
  return False
  
rules = parseRules(blocks[0])

tks = blocks[2].splitlines()
allInvalidValues = []
for i in range(1, len(tks)):
  tkFields = tks[i].split(",")
  invalidValues = []
  for v in tkFields:
    v = int(v)
    if not satisfiesARule(rules, v):
      invalidValues.append(v)
  allInvalidValues += invalidValues
  
theSum = 0
for v in allInvalidValues:
  theSum += v
print theSum