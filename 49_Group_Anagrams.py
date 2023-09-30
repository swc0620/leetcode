class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = {}
        for s in strs:
            s_tuple = ''.join(sorted(s))
        
            if s_tuple in res:
                res[s_tuple].append(s)
            else:
                res[s_tuple] = [s]
        
        return list(res.values())
