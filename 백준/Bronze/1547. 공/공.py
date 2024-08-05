import sys 
cnt = int(sys.stdin.readline())
cup = [1, 2, 3]
tmp = 0
i = 0
n = -1

while True:
    a, b = map(int, input().split())
    tmp = cup[a-1] 
    cup[a-1] = cup[b-1]
    cup [b-1] = tmp
    
    i += 1
    if (i == cnt):
        break 

while True:
    n += 1
    if (cup[n] == 1):
        print(n+1)
        break