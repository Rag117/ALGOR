str = input()

i = 0
j = 0
A = 1

for i in range(len(str)//2):
    if (str[j] == str[len(str) - (j+1)]):
        j += 1
    else:
        A = 0
        j += 1
        
if (A == 1):
    print('1')
elif (A == 0):
    print('0')