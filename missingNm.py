class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumMissing = 0
        sumFull = 0
        index = 1
        

        for i, num in enumerate(nums):
            sumMissing += num
            sumFull += i
            index = i

        sumFull += index+1

        return sumFull - sumMissing

    


