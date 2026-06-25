class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return -1
        else:
            idx_l = 0
            idx_r = len(nums) - 1

            while idx_l <= idx_r:
                idx_m = int((idx_l + idx_r) // 2)

                if nums[idx_m] == target:
                    return idx_m
                elif target > nums[idx_m]:
                    idx_l = idx_m + 1
                else:
                    idx_r = idx_m - 1
            
            return -1