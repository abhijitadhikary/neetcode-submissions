class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hm = dict()

        for c in s:
            hm[c] = hm.get(c, 0) + 1
        
        for c in t:
            if hm.get(c, 0) == 0:
                return False
            hm[c] -= 1
        return True