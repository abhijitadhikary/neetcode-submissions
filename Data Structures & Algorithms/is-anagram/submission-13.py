class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hm = dict()

        for index in range(len(s)):
            hm[s[index]] = hm.get(s[index], 0) + 1
            hm[t[index]] = hm.get(t[index], 0) - 1
        
        return sum(map(bool, hm.values())) == 0