cnt = int(input())

callmin = list(map(int, input().split()))

ys = 0
ms = 0
a1 = 0
a2 = 0
tot1 = 0
tot2 = 0

for i in range(cnt):
    ys = (callmin[a1] // 30) * 10
    ysn = callmin[a1] % 30
    if(ysn >= 0):
        ys += 10
        
    tot1 += ys
    a1 += 1
    
    ms = (callmin[a2] // 60) * 15
    msn = callmin[a2] % 60
    if(msn >= 0):
        ms += 15
        
    tot2 += ms
    a2 += 1
    
if(tot1 < tot2):
    print("Y", end = " ")
    print(tot1)
elif(tot1 == tot2):
    print("Y M", end = " ")
    print(tot1)
else:
    print("M", end = " ")
    print(tot2)