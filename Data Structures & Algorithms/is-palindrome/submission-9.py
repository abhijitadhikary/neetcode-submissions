class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        idx_l = 0
        idx_r = len(s) - 1

        while idx_l < idx_r:
            while not s[idx_l].isalnum() and idx_l < idx_r:
                idx_l += 1
            while not s[idx_r].isalnum() and idx_l < idx_r:
                idx_r -= 1
            
            if s[idx_l].lower() != s[idx_r].lower():
                return False
            idx_l += 1
            idx_r -= 1
        return True
            