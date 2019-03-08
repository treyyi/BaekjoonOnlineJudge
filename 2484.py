import collections;N=int(input())
_maximum = []
for _ in range(N):
    list = [*map(int, input().split())]
    a = [item for item in collections.Counter(list).items()]
    if len(set(list)) == 1:
        _maximum.append(50000+(list[0]*5000))
    elif len(set(list)) == 2 and (a[0][1] == a[1][1]):
        _maximum.extend([2000+(sum([item for item, count in collections.Counter(list).items() if count == 2]))*500])
    elif len(set(list)) == 2 and (a[0][1] != a[1][1]):
        _maximum.append(10000+([item for item, count in collections.Counter(list).items() if count == 3][0]*1000))
    elif len(set(list)) == 3:
        _maximum.append(1000+([item for item, count in collections.Counter(list).items() if count == 2][0]*100))
    elif len(set(list)) == 4:
        _maximum.append(max(list)*100)
print(max(_maximum))

        # Another way for else:
        # seen = set()
        # uniq = []
        # for x in list:
        #     if x not in seen:
        #         uniq.append(x)
        #         seen.add(x)
