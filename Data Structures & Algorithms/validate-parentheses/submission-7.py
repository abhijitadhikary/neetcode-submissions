class Solution:
    def isValid(self, s: str) -> bool:

        seen = []

        brackets_dict = {
            ")": "(",
            "]": "[", 
            "}": "{"
        }
        op = brackets_dict.values()
        for c in s:
            if c in op:
                seen.append(c)
            else:
                if len(seen) == 0 or brackets_dict[c] != seen.pop():
                    return False
        if len(seen) > 0:
            return False
        return True