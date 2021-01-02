with open('input.txt') as f:
  lines = f.read().splitlines()

na = [] 
for line in lines:
  na.append(int(line))

print na  
na.sort()
print na

jumps = [0, 0, 0, 0]
joltage = 0
for adapterRating in na:
  print joltage, adapterRating
  jump = adapterRating - joltage
  jumps[jump] += 1
  joltage = adapterRating
  
# add the jump from last adapter to device
jumps[3] += 1

print jumps[1] * jumps[3]