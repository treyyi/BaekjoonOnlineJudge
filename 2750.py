import sys
# Input Example
# 5 -> number of input line, which contains a single number
# 5
# 4
# 3
# 2
# 1
def bubble_sort(arr):
    # print(arr)
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j] < arr[j-1]:
                tmp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=tmp
                # print(arr)
    return arr

a=[]
for _ in range(int(input())):
    n=int(input())
    a.append(n)

for s in bubble_sort(a):
    print(s)
