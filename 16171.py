l=input();a=input();c=''
for s in l:
    try:
        int(s)
    except Exception:
        c+=s
print('1' if a in c else '0')
