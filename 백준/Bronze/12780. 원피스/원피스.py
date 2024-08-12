Pa = input()
cmp = input()

i = 0
a = 0
for i in range(len(Pa)-len(cmp)+1):
    if (Pa[0+i:len(cmp)+i] == cmp):
        a += 1

print(a)