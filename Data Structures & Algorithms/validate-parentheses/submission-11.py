class Solution:
    def isValid(self, s: str) -> bool:

        seen = []

        brackets_dict = {
            ")": "(",
            "]": "[", 
            "}": "{"
        }

        op = set(brackets_dict.values())

        for c in s:
            if c in op:
                seen.append(c)
            else:
                if not seen or brackets_dict[c] != seen.pop():
                    return False
        return not seen