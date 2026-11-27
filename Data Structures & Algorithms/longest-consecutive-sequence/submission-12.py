class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2 and nums[1]-nums[0] == 1:
            return 2
        nums = set(nums)

        len_max = 0
        for num in nums:
            if num-1 not in nums:
                len_c = 1
                while num + len_c in nums:
                    len_c += 1
                len_max = max(len_c, len_max)
        return len_max