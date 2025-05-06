T = int(input())

for i in range(T):
    string = input().split(" ")
    n = int(string[0])
    numofDrops = int(string[1])
    best_avr = 0
    worse_avr = 0
    gradeList = input().split(" ")
    best_sum = 0
    worse_sum = 0
    for i in range(len(gradeList)):
        gradeList[i] = int(gradeList[i])
    
    if n - numofDrops != 0:
        gradeList.sort()
        bestCase = gradeList
        worseCase = gradeList
        
        for i in range(numofDrops):
            bestCase.pop(0)
            worseCase.pop()
        
        for i in range(len(bestCase)):
            best_sum = best_sum + bestCase[i]
            worse_sum = worse_sum + worseCase[i]
            
        best_avr = round(float(best_sum / len(bestCase)), 2)    
        worse_avr = round(float(worse_sum / len(worseCase)), 2)
        print(f"{worse_avr:.2f} {best_avr:.2f}")
    
    else:
        print("0.00 0.00")