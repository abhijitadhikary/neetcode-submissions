class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(arr, idx_l, idx_r):
            if idx_l >= idx_r:
                return True
            if not arr[idx_l].isalnum():
                return check(arr, idx_l+1, idx_r)
            if not arr[idx_r].isalnum():
                return check(arr, idx_l, idx_r-1)
            if arr[idx_l].lower() == arr[idx_r].lower():
                return check(arr, idx_l+1, idx_r-1)
            return False
        return check(s, 0, len(s)-1)