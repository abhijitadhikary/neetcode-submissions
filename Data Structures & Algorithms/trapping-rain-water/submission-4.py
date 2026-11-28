class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = height[0]
        max_r = height[-1]
        idx_l = 0
        idx_r = len(height)-1

        total_trapped = 0

        while idx_l <= idx_r:
            if max_l < max_r:
                if height[idx_l] < max_l:
                    total_trapped += max_l - height[idx_l]
                else:
                    max_l = height[idx_l]
                idx_l += 1
            else:
                if height[idx_r] < max_r:
                    total_trapped += max_r - height[idx_r]
                else:
                    max_r = height[idx_r]
                idx_r -= 1
        return total_trapped