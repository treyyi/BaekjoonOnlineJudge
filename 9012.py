for _ in range(int(input())):
    flag = 1
    stack = []
    ps = list(input())

    for i in range(0, len(ps)):
        if ps[i] == "(":
            stack.append(1)
        elif ps[i] == ")":
            if len(stack) == 0:
                flag = 0
                break
            else:
                stack.pop()
    if len(stack) != 0:
        flag = 0

    if flag == 1:
        print("YES")
    else:
        print("NO")
