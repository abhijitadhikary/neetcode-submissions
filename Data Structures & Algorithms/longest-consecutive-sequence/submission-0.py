class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        nums.sort()
        
        max_len = 1
        counter = 1
        for idx in range(1, len(nums)):
            diff = nums[idx] - nums[idx - 1]
            if diff == 1:
                counter += 1
                max_len = max(counter, max_len)
                continue
            elif diff == 0:
                continue
            counter = 1
        return max_len
