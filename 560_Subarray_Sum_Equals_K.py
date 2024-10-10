class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, total_sum = 0, 0
        sum_map = {0: 1}

        for num in nums:
            total_sum += num
            if total_sum - k in sum_map:
                count += sum_map[total_sum - k]
            sum_map[total_sum] = sum_map.get(total_sum, 0) + 1
        return count
            
            