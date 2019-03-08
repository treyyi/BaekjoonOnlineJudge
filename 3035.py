r,c,x,y=map(int,input().split())
for _ in range(r):l=input();print((''.join(([h*y for h in l]))+'\n')*x,end='')


# R,C,ZR,ZC=map(int,input().split())
# lines=R*ZR+0**(C!=0)
# strings=''
# for _ in range(R):
#     tmp=''
#     for s in input():
#         tmp+=s*ZC
#     strings+=(tmp+'\n')*ZR
# print(strings)
