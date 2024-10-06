class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = sorted(list(map(str, nums)), reverse=True, key=lambda x: x*10)
        if str_nums and str_nums[0] == "0":
            return "0"
        return ''.join(str_nums)