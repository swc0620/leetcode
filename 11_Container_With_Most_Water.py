class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        vol = 0

        while True:
            if left == right:
                break
            
            h = min(height[left], height[right])
            vol = max((right-left)*h, vol)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return vol

