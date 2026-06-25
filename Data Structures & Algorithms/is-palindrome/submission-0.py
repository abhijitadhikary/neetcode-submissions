class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_stripped = "".join(c.lower() for c in s if c.isalnum())
        n = len(s_stripped)
        
        idx_l = 0
        idx_r = n - 1

        while idx_l < idx_r:
            if s_stripped[idx_l] != s_stripped[idx_r]:
                return False
            idx_l += 1
            idx_r -= 1
        return True

        