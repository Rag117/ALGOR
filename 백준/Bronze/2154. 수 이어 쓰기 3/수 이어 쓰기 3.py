num = int(input())
cmp = str(num)
arr = ''

for i in range(num):
    arr += str(i+1)
    
for j in range(len(arr)-len(cmp)+1):
    if (arr[j:len(cmp)+j] == cmp):
        print(j+1)
        break