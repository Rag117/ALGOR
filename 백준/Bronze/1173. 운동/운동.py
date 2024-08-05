arr = list(map(int, input().split()))
pulse = arr[1]
demin = 0
totalmin = 0
    
if((arr[1] + arr[3]) > arr[2]):
    print(-1)

else:
    while demin < arr[0]:
        if(pulse + arr[3]) <= arr[2]:
            pulse += arr[3]
            demin += 1
        else:
            pulse -= arr[4]
            if pulse < arr[1]:
                pulse = arr[1]
        totalmin += 1
    print(totalmin)