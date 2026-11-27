class Solution:
    def isPalindrome(self, s: str) -> bool:
        idx_a = 0
        idx_b = len(s)-1
        
        def check_alpha_numeric(x):
            return (ord(x) >= ord("a") and ord(x) <= ord("z")) or (ord(x) >= ord("0") and ord(x) <= ord("9"))

        while idx_a < idx_b:
            print(idx_a, idx_b)
            l = s[idx_a].lower()
            r = s[idx_b].lower()
            if not check_alpha_numeric(l):
                idx_a += 1
                continue
            if not check_alpha_numeric(r):
                idx_b -= 1
                continue
            if l != r:
                return False
            idx_a += 1
            idx_b -= 1
        return True