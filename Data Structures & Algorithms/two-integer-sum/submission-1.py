class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for idx_i in range(0,n-1):
            for idx_j in range(idx_i+1,n):
                if nums[idx_i] + nums[idx_j] == target:
                    return [idx_i, idx_j]