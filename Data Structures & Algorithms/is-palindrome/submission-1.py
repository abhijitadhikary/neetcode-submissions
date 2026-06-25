class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_stripped = "".join(c.lower() for c in s if c.isalnum())
        n = len(s_stripped)
        
        for idx in range(n//2):
            if s_stripped[idx] != s_stripped[n-idx-1]:
                return False
        return True
        