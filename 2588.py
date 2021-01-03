a = int(input())
b = str(int(input()))


first = a * int(b[-1])
second = a * int(b[1])
third =  a* int(b[0])

print(first)
print(second)
print(third)
print(first + (second*10) + (third*100))
