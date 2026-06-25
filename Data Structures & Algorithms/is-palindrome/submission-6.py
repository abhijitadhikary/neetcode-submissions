class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        idx_l = 0
        idx_r = len(s) - 1

        while idx_l < idx_r:
            if not s[idx_l].isalnum():
                idx_l += 1
                continue
            if not s[idx_r].isalnum():
                idx_r -= 1
                continue
            
            if s[idx_l].lower() != s[idx_r].lower():
                return False
            idx_l += 1
            idx_r -= 1
        return True
            