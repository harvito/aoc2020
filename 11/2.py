with open('input.txt') as f:
  lines = f.read().splitlines()
  
def occInDirection(row, col, dRow, dCol, seats):
  while (True):
    row += dRow
    col += dCol
    if seats[row][col] == '#':
      return True
    elif seats[row][col] == 'X':
      return False
    elif seats[row][col] == 'L':
      return False
    
  
def countAdjOccupied(row, col, seats):
  count = 0
  if occInDirection(row, col, -1, -1, seats):
    count += 1
  if occInDirection(row, col, -1, 0, seats):
    count += 1
  if occInDirection(row, col, -1, 1, seats):
    count += 1
  if occInDirection(row, col, 0, -1, seats):
    count += 1
  if occInDirection(row, col, 0, 1, seats):
    count += 1
  if occInDirection(row, col, 1, -1, seats):
    count += 1
  if occInDirection(row, col, 1, 0, seats):
    count += 1
  if occInDirection(row, col, 1, 1, seats):
    count += 1
  return count
  

oldSeats = [['X'] + list(n) + ['X'] for n in lines]
width = len(oldSeats[0])
oldSeats.insert(0, ['X'] * width)
oldSeats.append(['X'] * width)

# print oldSeats

newSeats = [list(n) for n in oldSeats]

changeWasMade = True
while changeWasMade:
  changeWasMade = False
  for row in oldSeats:
    print "".join(row)

  print "whee"
  for i in range(1, len(lines) + 1):
    for j in range(1, len(lines[0]) + 1):
      if (oldSeats[i][j] == 'L') and (countAdjOccupied(i, j, oldSeats) == 0):
        newSeats[i][j] = '#'
        changeWasMade = True
      elif (oldSeats[i][j] == '#') and (countAdjOccupied(i, j, oldSeats) >= 5):
        newSeats[i][j] = 'L'
        changeWasMade = True
      else:
        newSeats[i][j] = oldSeats[i][j]
  
  oldSeats = [list(n) for n in newSeats]

count = 0
for row in newSeats:
  for seat in row:
    if seat == '#':
      count += 1
print count

# 132 too low