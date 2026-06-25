class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        import numpy as np

        nums = np.array(nums)

        idx_sorted = np.argsort(nums)

        nums = nums[idx_sorted]

        idx_l = 0
        idx_r = len(nums) - 1

        while idx_l < idx_r:
            sum_c = nums[idx_l] + nums[idx_r]
            if sum_c == target:
                a = idx_sorted[idx_l]
                b = idx_sorted[idx_r]
                if a < b:
                    return [a, b]
                else:
                    return [b, a]
            else:
                if sum_c < target:
                    idx_l += 1
                else:
                    idx_r -= 1