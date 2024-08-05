import sys 
cnt = int(sys.stdin.readline())
sump = 0
plug = 0
i = 0

while True:
    plug = int(sys.stdin.readline())
    sump += plug
    
    i += 1
    if (i == cnt):
        break 
    
print(sump-(cnt-1)) 