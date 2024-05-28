class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = {}
        for t in target:
            res[t] = False

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for idx in range(len(triplet)):
                if triplet[idx] == target[idx]:
                    res[triplet[idx]] = True
            
        for val in res.values():
            if val == False:
                return False
        
        return True