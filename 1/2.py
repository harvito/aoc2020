print "hello world"

with open('input.txt') as f:
  lines = f.read().splitlines()
    
for a in lines:
  for b in lines:
    for c in lines:
      a = int(a)
      b = int(b)
      c = int(c)
      if a + b + c == 2020:
        print a, b, c, a * b * c
    
print lines