inputs = list(map(int, input().strip().split()))
A = inputs[0]
B = inputs[1]

if (A < B):
    num_of_ints = (B - A - 1)
    print(num_of_ints)
    for i in range(1, num_of_ints + 1):  # index starting from 1
        print(A + i, end=' ')
elif (A > B):
    num_of_ints = (A - B - 1)
    print(num_of_ints)
    for i in range(1, num_of_ints + 1):  # index starting from 1
        print(B + i, end=' ')
else:  # if A == B
    print("0")
