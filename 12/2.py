with open('input.txt') as f:
  lines = f.read().splitlines()

# x is positive to the East
# y is positive to the North
# facing is in degrees, positive ccw. 0 is East, 90 is North, 180 is West, and 270 is South.
x, y = 0, 0
dx, dy = 10, 1
for line in lines:
  c = line[0]
  v = int(line[1:])
  if c == 'N':
    dy += v
  elif c == 'S':
    dy -= v
  elif c == 'E':
    dx += v
  elif c == 'W':
    dx -= v
  elif (c in "LR") and (v == 180): # turn around
    print "turn around"
    dx = -dx
    dy = -dy
  elif line in "R270L90": # rotate to the right 90   
    print "turn right"
    t = dx
    dx = -dy
    dy = t
  elif line in "R90L270":
    print "turn left"
    t = dx
    dx = dy
    dy = -t
  elif c == 'F':
    x += (dx * v)
    y += (dy * v)
  else:
    print "FAIL"
print x, y
print abs(x) + abs(y)

# 285 too low
# 44534 too high