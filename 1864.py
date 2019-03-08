import sys

def calculate(arr):
    hash={'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}
    N_to_value = []
    result = 0
    for element in arr:
        N_to_value.append(hash[element])
    for i in range(len(N_to_value)):
        result = result + N_to_value[i]*(8**(len(N_to_value)-i-1))
    return (result)

while(1):
    N=sys.stdin.readline().strip()
    N_to_list = list(N)
    if N=='#':
        break
    else:
        result = calculate(N_to_list)
        print(result)
