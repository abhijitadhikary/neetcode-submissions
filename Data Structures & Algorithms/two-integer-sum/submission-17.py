class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for idx_a in range(len(nums)-1):
            for idx_b in range(idx_a+1, len(nums)):
                if nums[idx_a] + nums[idx_b] == target:
                    return [idx_a, idx_b]
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