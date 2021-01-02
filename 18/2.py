with open("input.txt") as f:
  lines = f.read().splitlines()
  
def getTerm(stringExpr, start):
  slicedString = stringExpr[start:]
  if slicedString[0] == '(':
    
    # get closing bracket index
    openBrList = []
    for i in range(1, len(slicedString)):
      if slicedString[i] == '(':
        openBrList.append('(')
      elif slicedString[i] == ')':
        if not openBrList: # pythonic way to tell if list is empty
          closingIndex = i
        else:
          openBrList.pop()
    
    thisTerm = evalString2(slicedString[1:closingIndex])
    cursorPos = start + closingIndex + 2
  else: # first char is a number
    splitString = slicedString.split()
    thisTerm = int(splitString[0])
    cursorPos = start + len(splitString[0]) + 1
  return thisTerm, cursorPos
  
def evalString2(stringExpr):
  # find all top-level multiplication symbols *
  openBrList = []
  starList = []
  for i in range(0, len(stringExpr)):
    if stringExpr[i] == '(':
      openBrList.append('(')
    elif stringExpr[i] == ')':
      openBrList.pop()
    elif stringExpr[i] == '*' and not openBrList:
      starList.append(i)
      
  if starList:
    prod = 1
    index = 0
    for star in starList:
      prod *= evalString2(stringExpr[index:star-1])
      index = star + 2
    prod *= evalString2(stringExpr[index:])
    return prod
  else:
    # there are no top level multiplication symbols *
    acc, cursorPos = getTerm(stringExpr, 0)
    
    while cursorPos < len(stringExpr):
      op = stringExpr[cursorPos]
      cursorPos += 2
      term, cursorPos = getTerm(stringExpr, cursorPos)
      if op == '+':
        acc += term
      elif op == '*':
        acc *= term
    return acc

mySum = 0  
for line in lines:
  evaluated = evalString2(line)
  mySum += evaluated
print mySum

# 149505780575 too low
# 8140591945077 too high
# 209335026987 juust right