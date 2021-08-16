def reverse(x):
    flag = False
        
    if x < 0:
        flag = True
            
    x = str(x)
        
    if len(x) < 2:
        return int(x)
        

    reversed = x[::-1]
        
        
    # for i in range(len(reversed)):
    #     if int(reversed[i]) == 0:
                
        
    if flag == True:
        reversed = -int(reversed[:-1])
        
    return (reversed)

print(reverse(123))
print(reverse(-123))
print(reverse(120))