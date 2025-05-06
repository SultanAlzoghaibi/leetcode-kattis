



array = [3,4,6]
space1 = abs(array[1] - array[0])
space2 = abs(array[2] - array[1])
count = 0

while (space1 > 1) or (space2 > 1):
    
    
    print(count)
    print("spaece: ")
    print(array)
    
    
    if space2 > space1:
        array[0] = array[1] + 1
    else:
        array[2] = array[1] - 1
    
    count += 1
    array.sort()
    space1 = array[1] - array[0]
    space2 = array[2] - array[1]
        
print(count)




