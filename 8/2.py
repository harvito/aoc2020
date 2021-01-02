def executeBoot(lines):
  ranList = []
  i = 0
  acc = 0
  while (True):
    if (i in ranList) or (i > len(lines)):
      return False, acc
    elif i == len(lines):
      return True, acc
      
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
  
with open('input.txt') as f:
  lines = f.read().splitlines()
  
print len(lines)
# make mutants
mutants = []
for i in range(len(lines)):
  line = lines[i]
  if "jmp" in line:
    mutatedLine = line.replace("jmp", "nop")
    prgCopy = list(lines)
    prgCopy[i] = mutatedLine
    mutants.append(prgCopy)
  elif "nop" in line:
    mutatedLine = line.replace("nop", "jmp")
    prgCopy = list(lines)
    prgCopy[i] = mutatedLine
    mutants.append(prgCopy)
print "number of mutants", len(mutants)

# run the mutants
for mutant in mutants:
  term, acc = executeBoot(mutant)
  print term, acc
  if term:
    print acc
    break
    
  
