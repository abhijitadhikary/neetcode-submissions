class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area_max = 0

        idx_l = 0
        idx_r = len(heights)-1

        while idx_l < idx_r:
            
            height_l = heights[idx_l]
            height_r = heights[idx_r]
            area_c = min(height_l, height_r) * (idx_r-idx_l)
            area_max = max(area_max, area_c)
            if height_l < height_r:
                idx_l += 1
            else:
                idx_r -= 1
        return area_max