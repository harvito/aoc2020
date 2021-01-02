with open('input.txt') as f:
  groups = f.read().split("\n\n")
  
count = 0
for group in groups:
  
  a = ""
  for answers in group.split():
    a += answers
  print a
  b = set(answers)
  ell = len(b)
  print "count before", count
  count += ell
  print "adding", ell
  print "count after", count
  
print count

# 4296 too low