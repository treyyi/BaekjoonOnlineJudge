#NEED TO REVIEW FOR INPUT METHOD
import sys
for i in sys.stdin:
    x,y=map(int,i.split())
    print("{:.2f}".format(x/y))


# NOT WORKING - WHAT CAUSES RUNTIME ERROR?
# import sys
# while(1):
#     a,b=map(int,sys.stdin.readline().split())
#     print("DEBUG: ",a,b)
