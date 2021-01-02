import sys

with open('input.txt') as f:
  lines = f.read().splitlines()

na = [] 
for line in lines:
  na.append(int(line))

print na  
na.sort()
print na
print max(na)

joltages = [0]
for adapterRating in na:
  startingLen = len(joltages)
  print startingLen
  for i in range(startingLen):
    if adapterRating - joltages[i] <= 3:
      joltages.append(adapterRating)
  # next, remove the joltages more than 3 below the current adapter
  joltages = [n for n in joltages if n >= (adapterRating - 3)]
  
  print adapterRating
  sys.stdout.flush()
  
joltages = [n for n in joltages if n == max(na)]
print len(joltages)