class Solution:

    def encode(self, strs: List[str]) -> str:
        c = chr(555)
        return "".join(f"{a}{c}" for a in strs)

    def decode(self, s: str) -> List[str]:
        c = chr(555)
        return s.split(c)[:-1]