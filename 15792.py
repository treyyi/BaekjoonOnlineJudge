from decimal import *
A,B=map(float, input().split(' '))
result = Decimal.from_float(A/B)
print(result)
