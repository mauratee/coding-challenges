
def isAnagram(s, t):
    s_dict = {}

    if len(s) != len(t):
        return False

    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1
        
    for char in t:
        if char in s_dict:
            if t.count(char) == s_dict[char]:
                continue
            else:
                return False
        else:
            return False
            
    
    return True

print(isAnagram('ab', 'a'))
print(isAnagram('cacc', 'acac'))