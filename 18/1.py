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