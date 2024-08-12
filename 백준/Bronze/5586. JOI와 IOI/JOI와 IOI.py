JAI = input()

i = 0
joi = 0
ioi = 0

for i in range(len(JAI)-2):
    if(JAI[i:i+3] == 'JOI'):
        joi += 1
    if (JAI[i:i+3] == 'IOI'):
        ioi += 1    

print(joi)
print(ioi)