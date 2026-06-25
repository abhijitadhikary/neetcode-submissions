class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1 or n > 1000:
            return False
        
        n_current = n
        seen = set()

        while n_current <= 1000:
            sum_current = 0
            for c in str(n_current):
                sum_current += int(c)**2
            if sum_current == 1:
                return True
            if sum_current in seen:
                return False
            else:
                seen.add(sum_current)
            n_current = sum_current
        return False
