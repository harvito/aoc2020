with open('input.txt') as f:
  lines = f.read().splitlines()

def maskThis(inp, m):
  retAddrs = [[]]
  for i in range(len(m)):
    if m[i] == '0':
      for a in retAddrs:
        a.append(inp[i])
    elif m[i] == '1':
      for a in retAddrs:
        a.append('1')
    elif m[i] == 'X':
      for j in range(len(retAddrs)):
        a = list(retAddrs[j])
        retAddrs[j].append('0')
        retAddrs.append(a + ['1'])
    else:
      print "FAIL"
  returnValue = [ "".join(n) for n in retAddrs ]
  print "input:"
  print "".join(inp)
  for a in returnValue:
    print a
  return returnValue

mem = {}
for line in lines:
  parts = line.split(" = ")
  if "mask" in parts[0]:
    mask = list(parts[1])
  elif "mem" in parts[0]:
    addr = int( parts[0][4:len(parts[0])-1] )
    addr = format(addr, '036b')
    addresses = maskThis(list(addr), mask)
    
    v = int(parts[1])
    for address in addresses:
      mem[address] = v

count = 0
for v in mem.values():
  count += v
  
print count

# 1440175326757 too low
# 3839007159440 too high
