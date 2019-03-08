test_case = input()
while(test_case != "0"):
    if test_case == ''.join(list(reversed(test_case))):
        print("yes")
    else:
        print("no")
    test_case = input()

# Another Solution
# while 1:
#     a=input()
#     if a=='0':break
#     if a==a[::-1]:print('yes')
#     else:print('no')
