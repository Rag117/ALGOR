while True:
    branch = list(map(int, input().split()))
    
    if branch[0] == 0:
        break
    
    totlea = 1   
    for i in range(branch[0]):
        bra = branch[2 * i + 1]
        cut = branch[2 * i + 2]
        totlea = totlea * bra - cut
    print(totlea)