import sys

def num_card(num1):
    string_array = []
    
    while True:
        string_array.append(num1)
            
        multi_num = 1
        
        string_num1 = str(num1)
        
        for i in range(len(string_num1)):
            multi_num *= int(string_num1[i])
            
        num1 = str(multi_num)
        
        if multi_num == 0 or multi_num < 10:
            break

    result = ' '.join(map(str, string_array))
    
    if string_array[0] != num1:
        result += f" {num1}"

    print(result)

while True:
    num1 = sys.stdin.readline().strip()
    
    if num1 == '0':  
        break

    num_card(num1)