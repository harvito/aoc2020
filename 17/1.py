import copy
import sys

with open("input.txt") as f:
  lines = f.read().splitlines()

def countActiveNeighbors(cube, x, y, z):
  num_actives = 0
  
  # count actives in 3x3x3 cube around x, y, z
  for plane in cube[z-1:z+2]:
    for row in plane[y-1:y+2]:
      for cell in row[x-1:x+2]:
        if cell == '#':
          num_actives += 1
  
  # remove cube[x][y][z] if it's active
  if cube[z][y][x] == '#':
    num_actives -= 1
    
  return num_actives

def printCube(cube):
  for z in range(len(cube)):
    print "z =", z - z0
    for y in cube[z]:
      print "".join(y)
    print ""

def padWithDots(cube):
  for z in range(len(cube)):
    for i in range(len(cube[0])):
      # pad left and right side with .
      cube[z][i].insert(0, '.')
      cube[z][i].append('.')

  # pad top and bottom with dots
  xLen = len(cube[0][0])
  rowOfDots = ['.'] * xLen
  for plane in cube:
    plane.insert(0, list(rowOfDots))
    plane.append(list(rowOfDots))

  # wrap the box with plane of dots on surface and floor
  yLen = len(cube[0])
  planeOfDots = [list(rowOfDots) for n in range(yLen)]
  cube.insert(0, copy.deepcopy(planeOfDots))
  cube.append(copy.deepcopy(planeOfDots))
  # z0 = 1
  
  return cube
  


cube = []
# when we need to insert a row at the beginning, increment the respective of these
x0 = 0
y0 = 0
z0 = 0

initialPlane = []
for line in lines:
  yList = list(line)
  initialPlane.append(yList)

cube.append(initialPlane)

print "no pad"
printCube(cube)
padWithDots(cube)
print "once padded"
printCube(cube)
padWithDots(cube)
print "twice padded"
printCube(cube)

#for z in range(1, len(cube)-1):
#  print "z =", z - z0
#  for y in range(1, len(cube[0])-1):
#    for x in range(1, len(cube[0][0])-1):
#      sys.stdout.write( str(countActiveNeighbors(cube, x, y, z)) )
#    print ""


newCube = copy.deepcopy(cube)

for i in range(6):
  for z in range(1, len(cube)-1):
    for y in range(1, len(cube[0])-1):
      for x in range(1, len(cube[0][0])-1):
        # print "i x y z", i, x, y, z
        if (cube[z][y][x] == '#'): # active
          if countActiveNeighbors(cube, x, y, z) in [2, 3]:
            newCube[z][y][x] = '#'
          else:
            newCube[z][y][x] = '.'
        elif cube[z][y][x] == '.': # inactive
          if countActiveNeighbors(cube, x, y, z) == 3:
            newCube[z][y][x] = '#'
          else:
            newCube[z][y][x] = '.'
          
        # sys.stdout.write( str(countActiveNeighbors(cube, x, y, z)) )
      # print ""
  padWithDots(newCube)
  printCube(newCube)
  cube = copy.deepcopy(newCube)
  
count = 0
for plane in cube:
  for row in plane:
    for c in row:
      if c == '#':
        count += 1
print count


