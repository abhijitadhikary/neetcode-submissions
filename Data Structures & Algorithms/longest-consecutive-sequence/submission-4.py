class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        nums = sorted(list(set(nums)))
        print(nums)
        
        count_max = 1
        count_c = 1

        for idx in range(1, len(nums)):
            diff = nums[idx] - nums[idx-1]
            if diff == 1:
                count_c += 1
                continue
            elif count_c > 0:
                count_max = max(count_c, count_max)
                count_c = 1
        count_max = max(count_c, count_max)
        return count_max