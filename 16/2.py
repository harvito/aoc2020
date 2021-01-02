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
  
def satisfiesTheseRules(rules, v):
  retRules = []
  for field, ranges in rules:
    for range in ranges:
      if range[0] <= v <= range[1]:
        retRules.append(field)
  return set(retRules)
  
rules = parseRules(blocks[0])

tks = blocks[2].splitlines()
maybeValidTks = []
for i in range(1, len(tks)):
  tkFields = tks[i].split(",")
  invalidValues = []
  tkValid = True
  for v in tkFields:
    v = int(v)
    if not satisfiesARule(rules, v):
      tkValid = False
  if tkValid:
    maybeValidTks.append(tks[i])
  
justRuleNames = []
for name, ranges in rules:
  justRuleNames.append(name)
fieldNCanBe = [set(justRuleNames)] * len(rules)
for tkFields in maybeValidTks:
  tkFields = tkFields.split(",")
  for i in range(len(tkFields)):
    ruleSet = satisfiesTheseRules(rules, int(tkFields[i]))
    fieldNCanBe[i] = ruleSet.intersection(fieldNCanBe[i])
  

for i in range(len(fieldNCanBe)):
  print "field", i, "can be", fieldNCanBe[i]

key = {}
stop = False
while not stop:
  stop = True
  for i in range(len(fieldNCanBe)):
    if len(fieldNCanBe[i]) == 1:
      stop = False
      (field,) = fieldNCanBe[i]
      key[field] = i
      for j in range(len(fieldNCanBe)):
        fieldNCanBe[j] -= set([field])
      break
        
for i in range(len(fieldNCanBe)):
  print "field", i, "can be", fieldNCanBe[i]
  
for k, v in key.items():
  print k, "is field", v
  
myTicket = blocks[1].splitlines()[1].split(",")
product = 1
for k, v in key.items():
  if "departure" in k:
    product *= int(myTicket[v])
print product


