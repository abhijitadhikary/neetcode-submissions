class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()

        n = len(s)
        m = len(t)

        if n != m:
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
            
            # for k, v in seen.items():
            #     if v != 0:
            #         return False
            return True
