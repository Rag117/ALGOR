cnt = int(input())

hlist = []
for i in range(cnt):
    dicelist = list(map(int, input().split()))
    
    if dicelist[0] == dicelist[1] and dicelist[1] == dicelist[2]:
        hlist.append(10000 + dicelist[0] * 1000)
    elif dicelist[0] == dicelist[1] :
        hlist.append(1000 + dicelist[0] * 100)
    elif dicelist[1] == dicelist[2]:
        hlist.append(1000 + dicelist[1] * 100)
    elif dicelist[0] == dicelist[2]:
        hlist.append(1000 + dicelist[0] * 100)
    else:
        hlist.append(max(dicelist) * 100)
    
print(max(hlist))