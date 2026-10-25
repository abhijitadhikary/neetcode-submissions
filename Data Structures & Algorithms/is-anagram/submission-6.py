class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = dict()
        for c in s:
            seen_s[c] = seen_s.get(c, 0) + 1
        
        for c in t:
            if c in seen_s.keys():
                seen_s[c] -= 1
            else:
                return False
        for v in seen_s.values():
            if v != 0:
                return False
        return True