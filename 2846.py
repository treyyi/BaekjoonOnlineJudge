N=int(input())
nums=list(map(int,input().split()))
ups=[]
max_height=0
count=0
for i in range(len(nums)-1):
    v = nums[i+1]-nums[i]
    if v > 0:
        max_height=max_height+v
        if i == len(nums)-2:  # to control the last index element
            ups.append(max_height)
    else:
        ups.append(max_height)
        max_height=0
print(max(ups))
