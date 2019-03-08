import sys
for i in sys.stdin:
    M,F=map(int,i.split())
    if M==0 and F==0:break
    print(M+F)
