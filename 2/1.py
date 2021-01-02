with open('input.txt') as f:
  lines = f.read().splitlines()
    
count = 0
for line in lines:
  parts = line.split(" ")
  min, max = parts[0].split("-")
  c = parts[1][0]
  d = parts[2].count(c)
  if int(min) <= d <= int(max):
    count += 1
  
print count