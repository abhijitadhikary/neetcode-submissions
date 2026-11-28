from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        candidates = set()
        for idx_m in range(1, len(nums)-1):
            idx_l = 0
            idx_r = len(nums)-1
            
            while idx_l < idx_r and idx_l != idx_m and idx_r != idx_m:
                sum_c = nums[idx_l] + nums[idx_m] + nums[idx_r]
                
                if sum_c == 0:
                    candidates.add(tuple(sorted([nums[idx_l], nums[idx_m], nums[idx_r]])))
                    idx_l += 1
                    idx_r -= 1
                elif sum_c > 0:
                    idx_r -= 1
                else:
                    idx_l += 1
        return [list(t) for t in candidates]