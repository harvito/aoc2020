TARGET_TURN_NUM = 30000000 # 30 million
TARGET_INDEX = TARGET_TURN_NUM - 1

nums = [1,12,0,20,8,16]
lastIndexes = {
  1: 1,
  12: 2,
  0: 3,
  20: 4,
  8: 5,
  16: 6
}

num = 0

for i in range(6, TARGET_TURN_NUM):
  # add to our list
  nums.append(num)
  
  
  # think about next one
  if num in lastIndexes:
    # next num should be the difference
    nextNum = i + 1 - lastIndexes[num]
  else:
    nextNum = 0
    
  lastIndexes[num] = i + 1
    
  num = nextNum
  

print nums[TARGET_INDEX]

# 66312 too high