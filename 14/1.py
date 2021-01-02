with open('input.txt') as f:
  lines = f.read().splitlines()

def maskThis(inp, m):
  for i in range(len(m)):
    if m[i] == '0':
      inp[i] = '0'
    elif m[i] == '1':
      inp[i] = '1'
    elif m[i] == 'X':
      pass
    else:
      print "FAIL"
  return int("".join(inp), 2)

mem = {}
for line in lines:
  parts = line.split(" = ")
  if "mask" in parts[0]:
    mask = list(parts[1])
  elif "mem" in parts[0]:
    addr = parts[0]
    v = int(parts[1])
    print v
    v = format(v, '036b')
    print v
    v = maskThis(list(v), mask)
    print v
    mem[addr] = v

count = 0
for v in mem.values():
  count += v
  
print count

# 7164399800935 too low