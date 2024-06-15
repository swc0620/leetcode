class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtracking(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if idx >= len(candidates) or total > target:
                return

            comb.append(candidates[idx])
            backtracking(idx+1, comb, total+candidates[idx])
            comb.pop()
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtracking(idx+1, comb, total)
        
        backtracking(0, [], 0)
        return res