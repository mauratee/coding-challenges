
def reverse(x):
       
    # create flag for negative
    flag = False
        
    # if int is negative, change flag to true
    if x < 0:
        flag = True
        # take absolute value of int
        x = abs(x)
        
    # if int greater than or equal to zero and less than 10, return int
    if x <= 0 and x < 10:
        return x
        
    # create list for digits
    num_list = []
        
    # add each digit to num list
    while x != 0:
        current_num = x % 10
        num_list.append(current_num)
        x = x //10
            
            
    # while numbers in num list, check if list ends in zeros and delete trailing zeros
    while num_list:
        if num_list[0] == 0:
            num_list.remove(0)
        else:
            break
        
    # convert each item in list to string
    num_list = map(str, num_list)
    # convert map object to a list
    num_list = list(num_list)
        
    # print(num_list)
        
    # join list of strings into one string
    digits_reversed = "".join(num_list)
    # convert string back to integer
    digits_reversed = int(digits_reversed)
        
    # check if number is outside the 32-bit integer range, per description instructions
    if digits_reversed > 2147483647:
        return 0
        
    # add negative back if flagged as neg
    if flag == True:
        digits_reversed = -digits_reversed
        
    return digits_reversed
        