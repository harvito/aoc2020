class SumTable:
  def sums(self):
    returnSums = []
    for num, sums in self.table:
      returnSums += sums
    return set(returnSums)
    
  def __init__(self, size):
    self.table = []
    self.size = size
    
  def add(self, n):
    
  
    # construct the new row by summing 
    newRow = []
    ceil = min(len(self.table), 25)
    for i in range(ceil):
      num, sums = self.table[i]
      newRow.append(num + n)
        
      if len(newRow) == 24:
        break
        
    # remove last element from each table entry
    if len(self.table) >= 25:
      self.table.pop()
      for i in range(len(self.table)):
        num, sums = self.table[i]
        sums.pop()
        self.table[i] = (num, sums)
    
    self.table.insert(0, (n, newRow))
    
    for row in self.table:
      print len(row[1]), row
    print ""

with open('input.txt') as f:
  lines = f.read().splitlines()
  
sumTable = SumTable(25)
for i in range(len(lines)):
  n = int(lines[i])
  print i, n, ":"
  if (i < 25) or n in (sumTable.sums()):
    sumTable.add(n)
  else:
    print n
    break
print "done"
    
# 129 too low
# 255 too low