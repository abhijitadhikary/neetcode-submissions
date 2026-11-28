class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area_max = 0

        idx_l = 0
        idx_r = len(heights)-1

        while idx_l < idx_r:
            area_max = max(area_max, min(heights[idx_l], heights[idx_r]) * (idx_r-idx_l))
            if heights[idx_l] < heights[idx_r]:
                idx_l += 1
            else:
                idx_r -= 1
        return area_max