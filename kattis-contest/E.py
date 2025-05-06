string = input().split(" ")

n = int(string[0])
m = int(string[1])

list2d = []

wordsList = []
for i in range(n):
    wordsList.append(input())

for i in range(m):
    list2d.append(input())


for i in range(m):
    stringList = list(input())
    
    list2d[i] = stringList

count = 0
for i in range(m):
    for j in range(m):
        
        valid = False
        for t in range(m):
            
            for word in wordsList:
                if list2d[i+t][j] != word[t]:
                    valid = False
                    break
                else:
                    valid = True
            
        if valid:
            count = count + 1
        
        # --------------  
        valid = False
        for b in range(m):
            
            for word in wordsList:
                if list2d[i-b][j] != word[b]:
                    valid = False
                    break
                else:
                    valid = True
            
        if valid:
            count = count + 1
            
        # --------------   
        valid = False
        for r in range(m):
            
            for word in wordsList:
                if list2d[i][j+r] != word[r]:
                    valid = False
                    break
                else:
                    valid = True
            
        if valid:
            count = count + 1
        
        
        # --------------  
        valid = False
        for l in range(m):
            
            for word in wordsList:
                if list2d[i][j-l] != word[l]:
                    valid = False
                    break
                else:
                    valid = True
         # --------------  
        if valid:
            count = count + 1
            
        
             
        
        

        
print(count)