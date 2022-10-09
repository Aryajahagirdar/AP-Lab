import re

txt = input()
if re.findall("^[a-zA-z]", txt) == re.findall("[a-zA-z]$", txt):
    print("YES")
else:
    print("NO")
