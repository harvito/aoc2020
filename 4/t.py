import re

s = "953"
# p = re.compile("[0-9]*")
num = re.match("[0-9]{3}", s)
if num:
  print num.group()