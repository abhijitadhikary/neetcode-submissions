class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_all = []
        for num in nums:
            if num in num_all:
                return True
            else:
                num_all.append(num)
        return False