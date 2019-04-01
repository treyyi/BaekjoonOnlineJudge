stack=[]

def push_cmd(x):
    global stack
    stack.append(x)

def pop_cmd():
    global stack
    if stack != []:
        a=stack.pop()
        print(a)
    else:
        print(-1)

def size_cmd():
    print(len(stack))

def empty_cmd():
    print(1 if len(stack)==0 else 0)

def top_cmd():
    print(stack[-1] if len(stack) != 0 else -1)

for i in range(int(input())):
    tmp=input()
    if "push" in tmp:
        cmd,num = tmp.split()
        num=int(num)
    else: cmd=tmp

    if cmd=="push": push_cmd(num)
    elif cmd=="pop": pop_cmd()
    elif cmd=="size": size_cmd()
    elif cmd=="empty": empty_cmd()
    elif cmd=="top": top_cmd()
