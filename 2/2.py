with open('input.txt') as f:
  lines = f.read().splitlines()
    
count = 0
for line in lines:
  parts = line.split(" ")
  p1, p2 = parts[0].split("-")
  p1 = int(p1)
  p2 = int(p2)
  c = parts[1][0]
  if (parts[2][p1-1] == c) != (parts[2][p2-1] == c):
    count += 1
  
print count