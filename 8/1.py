with open('input.txt') as f:
  lines = f.read().splitlines()
  
ranList = []
i = 0
acc = 0
  
while (True):
  if i in ranList:
    print acc
    break
    
  ranList.append(i)
    
  lineWords = lines[i].split()
  if lineWords[0] == "acc":
    acc += int(lineWords[1])
    i += 1
  elif lineWords[0] == "jmp":
    i += int(lineWords[1])
  elif lineWords[0] == "nop":
    i += 1
  else:
    print "FAIL."
    break
  
# 146 too low
# not -15