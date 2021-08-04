def rotateString(s, goal):
        
        start = s
        if s == goal:
            return True
        
        s = (s[1:]) + s[0]
        
        def shift_str(s):
            
            s = (s[1:]) + s[0]
            print(s)
            
            if s == goal:
                return True
            if s == start:
                return False
            
            return shift_str(s)
            
        return shift_str(s)

print(rotateString("abcde", "cdeab"))