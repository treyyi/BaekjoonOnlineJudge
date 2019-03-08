while(1):
    a=input().strip()
    if a=='#':break
    else:
        count = 0
        for char in a:
            if char in "aeiouAEIOU":
                count += 1
        print(count)
