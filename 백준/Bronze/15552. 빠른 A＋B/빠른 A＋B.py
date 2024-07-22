import sys 
cnt = int(sys.stdin.readline())
i = 0

while True:
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
    i += 1
    if (i == cnt):
        break