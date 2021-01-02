print "hello world"

with open('input.txt') as f:
  lines = f.read().splitlines()
    
for a in lines:
  for b in lines:
    a = int(a)
    b = int(b)
    if a + b == 2020:
      print a, b, a * b
    
print lines