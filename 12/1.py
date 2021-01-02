with open('input.txt') as f:
  lines = f.read().splitlines()

# x is positive to the East
# y is positive to the North
# facing is in degrees, positive ccw. 0 is East, 90 is North, 180 is West, and 270 is South.
x, y = 0, 0
facing = 0
for line in lines:
  c = line[0]
  v = int(line[1:])
  if c == 'N':
    y += v
  elif c == 'S':
    y -= v
  elif c == 'E':
    x += v
  elif c == 'W':
    x -= v
  elif c == 'L':
    facing = (facing - v) % 360
  elif c == 'R':
    facing = (facing + v) % 360
  elif c == 'F':
    if facing == 0:
      x += v
    elif facing == 90:
      y += v
    elif facing == 180:
      x -= v
    elif facing == 270:
      y -= v
    else:
      print "FAIL"
  else:
    print "FAIL"
print x, y
print abs(x) + abs(y)

# 2503 too high 
  