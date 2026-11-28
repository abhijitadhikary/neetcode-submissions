class Solution:
    def trap(self, height: List[int]) -> int:
        list_levels = []
        list_left_max = []
        list_right_max = []
        max_l = -float("inf")
        max_r = -float("inf")

        for h in height:
            max_l = max(max_l, h)
            list_left_max.append(max_l)
        for h in height[::-1]:
            max_r = max(max_r, h)
            list_right_max.append(max_r)
        list_right_max = list_right_max[::-1]


        for idx in range(len(height)):
            h_max_l = 0
            h_max_r = 0
            h_max_l = list_left_max[idx]
            h_max_r = list_right_max[idx]
            list_levels.append(min(h_max_l, h_max_r) - height[idx])
        return sum(list_levels)