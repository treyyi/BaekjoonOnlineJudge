import collections

N=int(input())
_maximum = []
for _ in range(N):
    list = [*map(int, input().split())]
    a = list[0]
    b = list[1]
    c = list[2]
    if len(set(list)) == 1:
        _maximum.append(10000+(list[0]*1000))
    elif len(set(list)) == 3:
        _maximum.append(max(list)*100)
    else:
        _maximum.append(1000+([item for item, count in collections.Counter(list).items() if count > 1][0]*100))
print(max(_maximum))

        # Another way for else:
        # seen = set()
        # uniq = []
        # for x in list:
        #     if x not in seen:
        #         uniq.append(x)
        #         seen.add(x)
