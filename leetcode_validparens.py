
def isValid(s):
    # create open_paren_tracker list
    # index tracker
        
    # create list of open chracters '(', '{', '['
    # list of closed characters ')', '}', ']'
        
    # loop over character in string:
        # if char in open:
            # open index in list
            # add to tracker
        # if char in close
            # if char index 
            # delete matching open from tracker
        
    # if tracker list is empty:
        # return True
    # else:
        # return false
            
    # counter = 0
        
    # open_char = ['(', '{', '[']
    # closed_char = [')', '}', ']']
        
    # for char in s:
    #     if char in open_char:
    #         counter += 1
    #     if char in closed_char:
    #         counter -= 1
        
    # if counter == 0:
    #     return True
    # else:
    #     return False

    # create dictionary of closing, matching open brackets
    paren_dict = {')':'(', '}':'{', ']':'['}
    # create set of only open brackets
    open_paren = set(paren_dict.values())
    # print(open_paren)

    openers_seen = []

    # loop over char in s:
    for char in s:
        # if char in open_paren:
        if char in open_paren:
            # add to openers_seen list
            openers_seen.append(char)
        # if char not in open_paren:
        elif char not in open_paren:
            # if openers_seen is empty: return False
            if openers_seen == []:
                return False
            # if closer matches most recent opener: pop openers_seen list and continue
            if openers_seen[-1] == paren_dict.get(char):
                openers_seen.pop()
            # if closer doesn't match most recent opener: return False
            else:
                return False
    
    return openers_seen == []
    
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))