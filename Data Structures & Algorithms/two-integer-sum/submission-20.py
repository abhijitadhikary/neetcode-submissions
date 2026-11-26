class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = {num: [] for num in nums}
        
        for index, num in enumerate(nums):
            ids[num].append(index)
        
        nums.sort()

        idx_l = 0
        idx_r = len(nums) - 1
        while idx_l < idx_r:

            sum_c = nums[idx_l] + nums[idx_r]

            if sum_c == target:
                return sorted([min(ids[nums[idx_l]]), max(ids[nums[idx_r]])])
                
            elif sum_c > target:
                idx_r -= 1
            else:
                idx_l += 1

        # for idx_a in range(len(nums)-1):
        #     for idx_b in range(idx_a+1, len(nums)):
        #         if nums[idx_a] + nums[idx_b] == target:
        #             return [idx_a, idx_b]
        # found = dict()

        # for index, num in enumerate(nums):
        #     diff = target - num

        #     if num in found:
        #         return [found[num], index]
            
        #     else: 
        #         found[diff] = index
            
            # if diff in found:
            #     return [found[diff], index]
            # else:
            #     found[num] = index