number = int(input())
numerator_array = []
demoniator_array = []

for i in range(1, 1000):
    for j in range(1, i+1):
        numerator_array.append(i-j+1)
        demoniator_array.append(j)

print(numerator_array[number-1])
print(demoniator_array[number-1])