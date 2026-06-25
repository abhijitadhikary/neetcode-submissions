class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for idx_p in range(len(nums)):
            sum_r = 0
            sum_l = 0
            for idx_l in range(idx_p):
                sum_l += nums[idx_l]
            for idx_r in range(idx_p+1, len(nums)):
                sum_r += nums[idx_r]
            if sum_r == sum_l:
                return idx_p
        return -1
        