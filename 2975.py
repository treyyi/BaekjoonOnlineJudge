def calculate(alist):
    balance = int(alist[0])
    action = alist[1]
    money = int(alist[2])
    if action == "W":
        new_balance = balance - money
        if new_balance < -200:  # bank rule
            return ("Not allowed")
        else:
            return (balance - money)
    else:
        return (balance + money)

done = "0 W 0"
while True:
    temp = input()
    if temp != done:
        alist = temp.strip().split()
        result = calculate(alist)
        print(result)
    else: break
