import re

with open('input.txt') as f:
  lines = f.read().split("\n\n")

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
  If cm, the number must be at least 150 and at most 193.
  If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
"""

def hgt(x):
  num = int(re.match("[0-9]+", x).group())
  if "cm" in x:
    return 150 <= num <= 193
  elif "in" in x:
    return 59 <= num <= 76
  else:
    return False
    
def hcl(x):
  print "<", x, ">"
  p = re.match("#[[0-9a-f]{6}$", x)
  if p:
    print '"', x, "\" matches!"
    return True
  else:
    print '"', x, "\" does not match"
    return False
    
def pid(x):
  p = re.match("[0-9]{9}$", x)
  if p:
    return True
  else:
    return False

rules = [
  ("byr", (lambda x: 1920 <= int(x) <= 2002)),
  ("iyr", (lambda x: 2010 <= int(x) <= 2020)),
  ("eyr", (lambda x: 2020 <= int(x) <= 2030)),
  ("hgt", hgt),
  ("hcl", hcl),
  ("ecl", (lambda x: ("amb" in x) or ("blu" in x) or ("brn" in x) or ("gry" in x) or ("grn" in x) or ("hzl" in x) or ("oth" in x))),
  ("pid", pid)
]
  
count = 0

rulehits = {
  "byr": 0,
  "iyr": 0,
  "eyr": 0,
  "hgt": 0,
  "hcl": 0,
  "ecl": 0,
  "pid": 0
}

for line in lines:
  infos = line.split()
  
  valid = True
  for c, rule in rules:
    recordExists = False
    for i in infos:
      if c in i:
        recordExists = True
        data = i.split(":")[1]
        if not rule(data):
          valid = False
        else:
          rulehits[c] += 1
    if not recordExists:
      valid = False
  if valid:
    count += 1

print count
print rulehits

# 127 is too high
# not 117