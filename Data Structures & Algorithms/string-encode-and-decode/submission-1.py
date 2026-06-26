class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{a}{chr(555)}" for a in strs)

    def decode(self, s: str) -> List[str]:
        return s.split(chr(555))[:-1]