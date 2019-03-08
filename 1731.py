N=int(input())
sqnc = []
for _ in range(N):
    num = int(input())
    sqnc.append(num)
ari_sqnc1 = sqnc[1]-sqnc[0]
ari_sqnc2 = sqnc[2]-sqnc[1]
geo_sqnc1 = sqnc[1]//sqnc[0]
geo_sqnc2 = sqnc[2]//sqnc[1]
if sqnc[0]*sqnc[2]==sqnc[1]**2:
    print(sqnc[-1]*geo_sqnc1)
else:
    print(sqnc[-1]+ari_sqnc1)
