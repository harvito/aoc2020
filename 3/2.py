with open('input.txt') as f:
  lines = f.read().splitlines()
  
cr = len(lines[0])

  
counts = [0, 0, 0, 0, 0]
dxs = [1, 3, 5, 7, 1]
xposes = [0, 0, 0, 0, 0]

for i in range(1, len(lines)):
  # update
  for j in range(4):
    xposes[j] += dxs[j]
  if i % 2 == 0:
    xposes[4] += dxs[4] 

  # carriage return if necessary
  for j in range(5):
    xposes[j] %= cr
  
  # count
  for j in range(4):
    if lines[i][xposes[j]] == '#':
      counts[j] += 1
      
  if (i % 2 == 0) and (lines[i][xposes[4]] == '#'):
    counts[4] += 1
  
prod = 1
for c in counts:
  prod *= c
print prod