N, M = map(int, input().split())

arr1 = []
arr2 = []

for i in range(N):
    f = list(map(int, input().split()))
    arr1.append(f)

for i in range(N):
    s = list(map(int, input().split()))
    arr2.append(s)

for i in range(N):
    for j in range(M):
        print(arr1[i][j] + arr2[i][j])