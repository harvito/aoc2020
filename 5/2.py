with open('input.txt') as f:
  lines = f.read().splitlines()
  
seats = range(1024)

highest = 0
for line in lines:
  row = ""
  col = ""
  for c in line:
    if c == 'F':
      row += '0'
    elif c == 'B':
      row += '1'
    elif c == 'R':
      col += '1'
    elif c == 'L':
      col += '0'
    else:
      print "FAIL"
    
  print row, col
  row = int(row, 2)
  col = int(col, 2)
  print row, col
  seatId = row * 8 + col
  print seatId
  seats.remove(seatId)
  
print seats