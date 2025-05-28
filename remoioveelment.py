
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        l = 0
        while l < len(nums) :
            print(f"l: {l}")
            print(f"num[l]: {nums[l]}")
            print(f"nums: {nums}")
            if nums[l] == val:
                nums.pop(l)
            else:
                l += 1

        return len(nums)
