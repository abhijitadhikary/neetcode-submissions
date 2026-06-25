class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        ret = []
        ord_a = ord("a")

        for s in strs:
            a = [0] * 26            
            for c in s:
                a[ord(c) - ord_a] += 1
            a = tuple(a)

            if a in seen.keys():
                seen[a].append(s)
            else:
                seen[a] = [s]
        return list(seen.values())