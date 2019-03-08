import math
def foo(i):
    a=1/math.factorial(i)
    if i==0:return a
    for j in range(i-1,-1,-1):
        a=a+1/math.factorial(j)
    return a

print("""n e
- -----------""")
for i in range(10):
    a=foo(i)
    if i<2:print("{} {}".format(i, int(a)))
    elif i==2:print("{} {:.1f}".format(i, a))
    else:print("{} {:.9f}".format(i, a))
