TARGET_TURN_NUM = 30000000
TARGET_INDEX = TARGET_TURN_NUM - 1

nums = [1,12,0,20,8,16]

def findLastIndex(e, l):
  for i in range(len(l)-2, -1, -1):
    if l[i] == e:
      return i
  return len(l)-1

for i in range(6, 2021):
  lastIndex = findLastIndex(nums[-1], nums)
  
  if lastIndex == len(nums)-1:
    # new number, say 0
    nums.append(0)
  else:
    # repeated number, say difference
    nums.append(len(nums) - 1 - lastIndex)

print nums[TARGET_INDEX]

# not 8