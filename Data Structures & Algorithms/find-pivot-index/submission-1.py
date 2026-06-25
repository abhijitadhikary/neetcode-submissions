class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_prefix = [0]
        for num in nums:
            nums_prefix.append(nums_prefix[-1] + num)

        for idx_p in range(len(nums)):
            if nums_prefix[idx_p] == (nums_prefix[-1] - nums_prefix[idx_p+1]):
                return idx_p
        return -1