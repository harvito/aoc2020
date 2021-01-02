with open('input.txt') as f:
  lines = f.read().split("\n\n")

# byr
# iyr
# eyr
# hgt
# hcl
# ecl
# pid
  
count = 0

for s in lines:
  if ("byr" in s) and ("iyr" in s) and ("eyr" in s) and ("hgt" in s) and ("hcl" in s) and ("ecl" in s) and ("pid" in s):
    count += 1

print count