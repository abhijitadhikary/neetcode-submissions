class Solution:
    def trap(self, height: List[int]) -> int:
        area_total = 0
        stack = []

        for idx_r in range(len(height)):
            while stack and height[idx_r] > height[stack[-1]]:
                idx_u = stack.pop()
                if not stack:
                    break
                idx_l = stack[-1]

                area_total += (min(height[idx_l], height[idx_r]) - height[idx_u]) * (idx_r - idx_l - 1)

            stack.append(idx_r)
        return area_total