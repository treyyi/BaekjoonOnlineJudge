l=[i for i in range(1,31)];a=[]
for _ in range(28):
    a.append(int(input()))
print('\n'.join([str(x) for x in l if x not in a]))
