with open('input.txt') as f:
  lines = f.read().splitlines()
  
cr = len(lines[0])

  
count = 0
xpos = 0

lines.pop(0) # ignore first line
for line in lines:
  xpos = (xpos+3) % cr
  
  if line[xpos] == '#':
    count += 1
  
print count