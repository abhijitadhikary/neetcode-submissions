class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s = dict()
        dict_t = dict()

        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        
        return dict_s.items() == dict_t.items()
        

        