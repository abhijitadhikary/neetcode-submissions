class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        idx_l = 0
        idx_r = len(s) - 1

        while idx_l < idx_r:
            l = s[idx_l]
            r = s[idx_r]
            if not l.isalnum():
                idx_l += 1
                continue
            if not r.isalnum():
                idx_r -= 1
                continue
            
            if l.lower() != r.lower():
                return False
            idx_l += 1
            idx_r -= 1
        return True
            