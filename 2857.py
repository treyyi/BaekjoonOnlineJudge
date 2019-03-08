count=1
f=[]
for _ in range(5):
  a=input()
  if "FBI" in a:f.append(str(count))
  count+=1
if f == []:print("HE GOT AWAY!")
else:print(' '.join(f))
