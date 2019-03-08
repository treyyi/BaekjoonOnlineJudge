for _ in range(3):
 marker=[*map(int, input().split())];zeros=marker.count(0)
 if zeros==1:print("A")
 elif zeros==2:print("B")
 elif zeros==3:print("C")
 elif zeros==4:print("D")
 elif zeros==0:print("E")
