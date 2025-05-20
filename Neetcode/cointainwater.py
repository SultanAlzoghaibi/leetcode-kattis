class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) - 1
        l = 0
        max_Area = 0

        while l <= r:
            
            w = abs(r - l) 
            h = min(height[r], height[l])
            area = w * h

            if max_Area < area:
                max_Area = area

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        
        return max_Area
