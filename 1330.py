result = list(map(int, input().strip().split()))
compareResult = result[0] < result[1]
compareResult2 = result[0] > result[1]
if compareResult: print("<") elif compareResult2: print(">")
else: print("==")
