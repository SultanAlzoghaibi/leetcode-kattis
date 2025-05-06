nums = [-1,0,3,5,9,12]

target = 9

l = 0
r = len(nums) - 1
m = (len(nums)-1)//2
res = -1

print(f"r: {r}")
print(f"l: {l}")
print(f"m: {m}") 
print("start loop")

escape = False
while r > l:
    
    print(f"r: {r}")
    print(f"l: {l}")
    print(f"m: {m}") 

    if nums[m] == target:
        res = m
        print(nums[m])
        escape = True

    elif target > nums[m]:
        l = m + 1

    elif target < nums[m]:
        r = m - 1


    m = (r + l)//2
    
    
print("the res: ")
print(res)