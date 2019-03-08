a,b,c=input().split()
if a=="true":a="True"
else:a="False"
if b=="AND":b="and"
else:b="or"
if c=="true":c="True"
else:c="False"
print(str(eval(a+' '+b+' '+c)).lower())

# Short Coding
# a,b,c=input().split();a=a=='true';c=c=='true';print('true' if (a and c if b == 'AND' else a or c) else 'false')
