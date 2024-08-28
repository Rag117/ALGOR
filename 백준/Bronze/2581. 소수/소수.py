M = int(input())
N = int(input())
dem = []
check = 0

for i in range(M, N+1):
    check = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                check += 1
                break
        if check == 0: 
            dem.append(i)

if (sum(dem) <= 0):
    print(-1)
else:
    print(sum(dem))
    print(dem[0])