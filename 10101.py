a=[]
for _ in range(3):
    a.append(int(input()))
if set(a)=={60}:print("Equilateral")
elif sum(a)==180 and len(set(a))==2:print("Isosceles")
elif sum(a)==180 and len(set(a))==3:print("Scalene")
else:print("Error")
