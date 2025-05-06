


def ispalidrome(s):
    newStr= ""
    for char in s:
        if c.isalnum():
            newStr = newStr + c.lower
            
    return newStr == newStr[::-1]
    
    
def ispalidromev2(s):
    r = 0
    l = len(s)  - 1
    while l < r:  
        while l < r and not self.alphaNum(s[r]):
            r += 1
                 
        while l < r and not self.alphaNum(s[l]):
            l += 1
    
        
        if s[R].lower != s[L].lower:
            return False
        l += 1
        r += 1
#       
    return True
   
    


def alphaNum(self, char):
    return (ord('A') <= ord(char) <= ord('Z') or
    ord('a') <= ord(char) <= ord('z') or
    ord('0') <= ord(char) <= ord('9')) 
    
    
    char.lowe


# dfe lol(s):    
#     s = s.replace(" ","")
#     s = s.lower()

#     print(s)
    
#     for i in range(len(s)):
    
#         R_skip = 0
#         L_skip = 0
#         R = int(i)
#         L = int(len(s)) - int(i) - 1
        
#         print(i)
#         if not s[R].isalpha():
#             R_skip = R_skip + 1
#             R = i + R_skip
#             print("R-MOVED")
            
#         if not s[L].isalpha():
#             L_skip = L_skip + 1
#             L = len(s)-1 - i - R_skip
#             print("L-MOVED")
        
#         if s[R+R_skip] == s[L-L_skip]:
#             pass
#         else:
#             ans = "false"
            
#         if R >= L:
#             break


