sin = 0

while True:
    sin += 1
    state = 0
    o, w = map(int, input().split())
    
    if o == 0 and w == 0:
        break
    
    while True:
        st, num = input().split()
        if st == '#' and num == '0':
            break
        num = int(num)   
        if st == 'E':
            w -= num
        elif st == 'F':
            w += num
        if w <= 0:
            state = 1


    print(sin, end = " ")
    
    if(state == 1):
        print("RIP")
    else:
        if o/2 < w < o*2:
            print(":-)")
        else:
            print(":-(")