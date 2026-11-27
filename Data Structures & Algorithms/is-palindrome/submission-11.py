class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s_new = ""
        for c in s:
            if (ord(c) >= ord("a") and ord("c") <= ord("z")) or (ord(c) >= ord("0") and ord(c) <= ord("9")):
                s_new += c
        print(s)
        print(s_new)
        return s_new == s_new[::-1]