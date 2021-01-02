with open('input.txt') as f:
  lines = f.read().splitlines()

na = [] 
for line in lines:
  na.append(int(line))
  
TARGET = 15353384

i, j = 0, 0
while (True): # if sum < target, add above. if sum > target, remove below. if sum = target, stop.
  # sub = na[i:j+1]
  s = sum( na[i:(j+1)] )
  if s < TARGET:
    j += 1
  elif s == TARGET:
    subList = na[i:j+1]
    print subList
    print min(subList) + max(subList)
    break
  else: # s > TARGET
    i += 1
 
 # 1396138 too low