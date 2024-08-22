a, b = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(a-1, 0, -1): 
    for j in range(i): 
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            cnt += 1
            if cnt == b:
                print(f'{arr[j]} {arr[j+1]}')
                exit()
print(-1)