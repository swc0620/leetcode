# from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # with Counter
        # if Counter(s) != Counter(t):
        #     return False
        
        # return True

        # without Counter
        s_dict, t_dict = {}, {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        return s_dict == t_dict
        