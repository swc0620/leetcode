class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if idx >= len(candidates) or total > target:
                return
            
            comb.append(candidates[idx])
            backtracking(idx, comb, total+candidates[idx])
            comb.pop()
            backtracking(idx+1, comb, total)
        
        backtracking(0, [], 0)
        return res
