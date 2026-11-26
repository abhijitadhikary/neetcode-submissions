class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count = [0] * 26
        ord_a = ord('a')
        for c in s:
            count[ord(c.lower()) - ord_a] += 1
        for c in t:
            count[ord(c.lower()) - ord_a] -= 1
        return sum(map(bool, count)) == 0
        