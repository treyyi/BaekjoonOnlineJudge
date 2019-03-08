import sys
for i in sys.stdin:
    s=''.join(i.split())
    if s=='*':break
    if len(set(s)) < 26:print("N")
    else:print("Y")
