a, b = map(int, input().split())
arr = list(map(int, input().split()))
real = 0
cnt = 0

for i in range(a-1, 0, -1):
    real = arr.index(max(arr[:i+1]))
    if real != i:
        arr[i], arr[real] = arr[real], arr[i]
        cnt += 1        
        if cnt == b:
            print(*arr)
            exit()
print(-1)