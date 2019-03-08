def find_n4(n0):
    n1 = 3*n0
    n1_is_even = False
    odd_even = "odd"
    if n1 % 2 == 0:
        n2 = n1//2
        n1_is_even = True
        odd_even = "even"
    else:
        n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    return (odd_even, n4)
    # How to figure out n0
    # if n1_is_even:
    #     n0 = 2*n4
    # else:
    #     n0 = (2*n4)+1

count = 0
while True:
    n0 = int(input().strip())
    if n0 == 0:
        break
    else:
        count += 1
        odd_even, n4 = find_n4(n0)
        print('{}. {} {}'.format(count, odd_even, n4))
