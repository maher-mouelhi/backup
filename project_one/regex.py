import re

print(re.match("[0-9a-f]","a"))
print(re.match("[0-9a-f]","5"))

print(re.match("[0-9a-f]","z"))
print(re.match("[0-8]","9"))