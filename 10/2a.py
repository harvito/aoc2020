import sys



with open('input.txt') as f:
  lines = f.read().splitlines()

na = [] 
for line in lines:
  na.append(int(line))

print na  
na.sort()
print na
MAX_ADAPTER_RATING = max(na)

memo = [0] * (MAX_ADAPTER_RATING + 1)
memo[0] = 1

def memoize(n):
  if n == 1:
    memo[1] = 1
  elif n == 2:
    memo[2] = memo[1] + 1
  elif n == 3:
    memo[3] = memo[2] + memo[1] + 1
  else:
    memo[n] = memo[n-1] + memo[n-2] + memo[n-3]
  

"""
for each adapterRating, how many ways are there to reach this rating?
# eg with 1, 3, 4, 6:
# 1, there is 1 way
# 3, there are 2 ways: direct or 1.
# 4, there are 3 ways: from 1, from 3, or 1 -> 3. This is numWays(1) + numWays(3). In general, numWays(n) = numWays(n-1) + numWays(n-2) + numWays(n-3)
# 6, there are 4 ways: 1 -> 4, 1 -> 3, 3, 1 -> 3 -> 4

"""

for n in na:
  memoize(n)

print memo[MAX_ADAPTER_RATING]