A, B = sorted(map(int, input().split()))
nums = B - A + 1
if nums%2 == 0:  #even
    result = (A+B)*((nums)//2)
else:  #odd
    result = (A+B)*((nums)//2)+((A+B)//2)
print(result)
