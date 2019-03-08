import sys
n = int(input())
for _ in range(n):
    binary = sys.stdin.readline().strip()[::-1]
    decimal = 0
    for i in range(len(binary)):
        if binary[i] != "0":
            decimal = decimal + 2**i
    print(decimal)
