nums=[]
for _ in range(7):
    num=int(input())
    nums.append(num)
sorted_nums = sorted(nums)
odds_nums = []
odd_sum = 0
for item in sorted_nums:
    if item%2 != 0:
        odds_nums.append(item)
        odd_sum = odd_sum + item
if odd_sum == 0:
    print(-1)
else:
    print(odd_sum)
    print(min(odds_nums))
