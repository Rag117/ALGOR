KMP = input()
i = 0
print(KMP[0] ,end="")
for i in range(len(KMP)):
    if(KMP[i] == "-"):
        print(KMP[i+1], end= "")