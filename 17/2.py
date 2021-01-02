import copy
import sys

with open("input.txt") as f:
  lines = f.read().splitlines()

def countActiveNeighbors(cube, x, y, z, w):
  num_actives = 0
  
  # count actives in 3x3x3x3 hypercube around x, y, z, w
  for time in cube[w-1:w+2]:
    for plane in time[z-1:z+2]:
      for row in plane[y-1:y+2]:
        for cell in row[x-1:x+2]:
          if cell == '#':
            num_actives += 1
  
  # remove cube[x][y][z] if it's active
  if cube[w][z][y][x] == '#':
    num_actives -= 1
    
  return num_actives

def printCube(cube):
  for w in range(len(cube)):
    for z in range(len(cube[0])):
      print "w, z =", w, z
      for y in cube[w][z]:
        print "".join(y)
      print ""

def padWithDots(cube):
  for time in cube:
    for plane in time:
      for row in plane:
        # pad left and right side with .
        row.insert(0, '.')
        row.append('.')

  # pad top and bottom with dots
  xLen = len(cube[0][0][0])
  rowOfDots = ['.'] * xLen
  for time in cube:
    for plane in time:
      plane.insert(0, list(rowOfDots))
      plane.append(list(rowOfDots))

  # wrap the box with plane of dots on surface and floor
  yLen = len(cube[0][0])
  planeOfDots = [list(rowOfDots) for n in range(yLen)]
  for time in cube:
    time.insert(0, copy.deepcopy(planeOfDots))
    time.append(copy.deepcopy(planeOfDots))
    
  # add a cube of dots before and after
  zLen = len(cube[0])
  cubeOfDots = [copy.deepcopy(planeOfDots) for n in range(zLen)]
  cube.insert(0, copy.deepcopy(cubeOfDots))
  cube.append(copy.deepcopy(cubeOfDots))
  
  


cube = [[]]
# when we need to insert a row at the beginning, increment the respective of these
x0 = 0
y0 = 0
z0 = 0

initialPlane = []
for line in lines:
  yList = list(line)
  initialPlane.append(yList)

cube[0].append(initialPlane)

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
  for w in range(1, len(cube)-1):
    for z in range(1, len(cube[0])-1):
      for y in range(1, len(cube[0][0])-1):
        for x in range(1, len(cube[0][0][0])-1):
          # print "i x y z", i, x, y, z
          if (cube[w][z][y][x] == '#'): # active
            if countActiveNeighbors(cube, x, y, z, w) in [2, 3]:
              newCube[w][z][y][x] = '#'
            else:
              newCube[w][z][y][x] = '.'
          elif cube[w][z][y][x] == '.': # inactive
            if countActiveNeighbors(cube, x, y, z, w) == 3:
              newCube[w][z][y][x] = '#'
            else:
              newCube[w][z][y][x] = '.'
            
          # sys.stdout.write( str(countActiveNeighbors(cube, x, y, z)) )
        # print ""
  padWithDots(newCube)
  printCube(newCube)
  cube = copy.deepcopy(newCube)
  
count = 0
for time in cube:
  for plane in time:
    for row in plane:
      for c in row:
        if c == '#':
          count += 1
print count


