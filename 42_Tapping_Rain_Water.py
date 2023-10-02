class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        volume = 0
        max_left, max_right = height[left], height[right]

        while left < right:
            if max_left <= max_right:
                volume += (max_left - height[left])
                left += 1
                max_left = max(height[left], max_left)
            else:
                volume += (max_right - height[right])
                right -= 1
                max_right = max(height[right], max_right)
        
        return volume