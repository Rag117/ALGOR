test_center = int(input())
investigator = list(map(int, input().split()))
assign = list(map(int, input().split()))

tot_assign = 0

for i in range(test_center):
    tot_assign += 1
    after_assign = investigator[i] - assign[0]
    
    if after_assign > 0:
        if after_assign % assign[1] > 0:
            tot_assign += after_assign // assign[1] + 1
        if after_assign % assign[1] == 0:
            tot_assign += after_assign // assign[1] 
        
print(tot_assign)