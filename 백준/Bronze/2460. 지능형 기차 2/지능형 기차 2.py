i = 0
sum1 = 0
max = 0
while True:
    a, b = map(int, input().split())
    sum1 = (sum1-a+b)

    if (max < sum1):
        max = sum1
    
    i += 1
    if (i == 10):
        break 

print(max)