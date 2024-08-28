a, b = input().split()

bin_sum = bin(int(a,2) + int(b,2)) 

print(bin_sum[2:])