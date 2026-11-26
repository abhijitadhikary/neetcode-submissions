class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                return True
        return False