import re
def solve(s):
    matches = re.findall("(\d+)", s)
    highest = 0
    for i in matches:
        if int(i) > int(highest):
            highest = i
        else:
            pass
    return int(highest)