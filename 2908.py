a,b = map(str, input().split())
reversed = [int(a[::-1]), int(b[::-1])]
print(max(reversed))
