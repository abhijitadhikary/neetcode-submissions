class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_stripped = "".join(c.lower() for c in s if c.isalnum())
        return s_stripped == s_stripped[::-1]