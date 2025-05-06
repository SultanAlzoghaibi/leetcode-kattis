input1 = input().split(" ")

t = int(input1[0])

n = int(input1[1])
list_of_times = []
for i in range(n):
    
    string = input().split(" ")
    time = int(string[1])
    list_of_times.append(time)
    
print(list_of_times)
list_of_times.sort()
print(list_of_times)

duration = 0
i = 0

for i in range(n):
    duration = duration + list_of_times[i]
    
    if(t < duration):
        break
    i = i + 1
    
print(i)
    
