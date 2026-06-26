class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        idx = 0
        
        list_ret = []
        while idx < len(s):
            str_c = ""
            while s[idx] != "#":
                str_c += s[idx]
                idx += 1
            len_c = int(str_c) + idx

            str_c = ""
            idx += 1
            while idx <= len_c:
                str_c += s[idx]
                idx += 1
            list_ret.append(str_c)
        return list_ret