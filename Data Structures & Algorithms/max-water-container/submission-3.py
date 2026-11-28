class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area_max = 0

        indices = sorted(range(len(heights)), key=lambda x: heights[x], reverse=True)
        
        idx_left = indices[0]
        idx_right = indices[0]

        for idx in range(1, len(heights)):
            width = max(abs(indices[idx] - idx_left), abs(indices[idx] - idx_right))
            height = heights[indices[idx]]

            area_max = max(area_max, height*width)
            idx_left = min(indices[idx], idx_left)
            idx_right = max(indices[idx], idx_right)

        return area_max