class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return chr(556)
        ret_str = ""
        for s in strs:
            ret_str += f"{s}{chr(555)}"
        return ret_str[:-1]


    def decode(self, s: str) -> List[str]:
        if s == chr(556):
            return []
        ret_arr = s.split(chr(555))
        return ret_arr