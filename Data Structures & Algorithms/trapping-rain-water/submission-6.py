class Solution:
    def trap(self, height: List[int]) -> int:
        area_total = 0
        stack = []

        for idx_r in range(len(height)):
            while stack and height[stack[-1]] < height[idx_r]:
                idx_b = stack.pop()
                if not stack:
                    break
                idx_l = stack[-1]
                height_c = min(height[idx_l], height[idx_r]) - height[idx_b]
                width_c = idx_r - idx_l - 1
                area_c = height_c * width_c
                area_total += area_c
                
            stack.append(idx_r)
        return area_total