class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()

        if len(s) != len(t):
            return False
        else:
            for alph in s:
                seen[alph] = seen.get(alph, 0) + 1
            for alph in t:
                if alph in seen:
                    seen[alph] -= 1
                    if seen[alph] < 0:
                        return False
                else:
                    return False
            
            return True
