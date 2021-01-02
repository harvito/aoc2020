with open('input.txt') as f:
  lines = f.read().splitlines()

earliestDeparture = int(lines[0])

buses = []
# stringBuses = lines[1].split(",")
for bus in (lines[1].split(",")):
  if bus == "x":
    pass
  else:
    buses.append(int(bus))
    
buses.sort()

waitTimes = [ n - (earliestDeparture % n) for n in buses ]

index = waitTimes.index(min(waitTimes))

print buses[index], waitTimes[index]
print buses[index] * waitTimes[index]

# not 3
# not 13
# 156 too low