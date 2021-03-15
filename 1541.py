input = input()
if '-' in input:
    subs = input.split('-')

    subs_sum = 0
    for i in range(1, len(subs)):
        if '+' in subs[i]:
            subs_sum += sum(map(int, subs[i].split('+')))
        else:
            subs_sum += int(subs[i])
    first_sum = sum(map(int, subs[0].split('+')))
    print(first_sum-subs_sum)
else:
    print(sum(map(int, input.split('+'))))

# nums = input()
# arr = []
# temp_num = ''
# count = 1
# for s in nums:
#     if s not in "-+":
#         temp_num += s
#         if count == len(nums):
#             arr.append(int(temp_num))
#     else:
#         arr.append(int(temp_num))
#         temp_num=''
#         arr.append(s)
#     count += 1

# temp_sum = 0
# for i in range(len(arr)):
#     if arr[i] not in "-+":
#         temp_sum += arr[i+1]
# print(arr[0]-temp_sum)
