class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        ret = []
        for s in strs:
            ss = "".join(i for i in sorted(s))
            if ss in seen.keys():
                seen[ss].append(s)
            else:
                seen[ss] = [s]
        return list(seen.values())