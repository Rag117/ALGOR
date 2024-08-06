cnt = int(input())

for _ in range(cnt):
    a, b = map(int, input().split())
    a2 = a % 10
    
    if a2 == 0:
        print(10)
    elif a2 == 1 or a2 == 5 or a2 == 6:
        print(a2)
    elif a2 == 4 or a2 == 9:
        if (b % 2 == 0):
            print((a2 * a2) % 10)
        else:
            print(a2)
    else:
        if b % 4 == 0:
            print(a2 ** 4 % 10)
        else:
            print(a2 ** (b % 4) % 10)
