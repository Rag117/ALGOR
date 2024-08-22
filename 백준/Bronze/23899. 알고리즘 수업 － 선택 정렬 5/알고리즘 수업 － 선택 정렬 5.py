a = int(input())
arr = list(map(int, input().split()))
cmp = list(map(int, input().split()))
real = 0

for i in range(a-1, 0, -1):
    if arr == cmp:
        break
    real = arr.index(max(arr[:i+1]))
    if real != i:
        arr[i], arr[real] = arr[real], arr[i]       
        
if arr == cmp:
    print(1)
else:
    print(0)