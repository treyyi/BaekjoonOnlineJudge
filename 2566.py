max_num=0
count=1
track_list = []
for _ in range(9):
    line=[*map(int,input().split())]
    if max_num < max(line):
        index2=line.index(max(line))+1
        track_list=[count, index2]
        max_num=max(line)
    count+=1
print(max_num)
print("{} {}".format(track_list[0], track_list[1]))

# Better approach
# l = []
# max = 0
# maxi = 0
# maxj = 0
#
# for i in range(9):
#     l.append([int(x) for x in input().split()])
#
# for i in range(9):
#     for j in range(9):
#         if l[i][j] > max:
#             max = l[i][j]
#             maxi = i
#             maxj = j
#
# print(max)
# print(maxi + 1, maxj + 1)
