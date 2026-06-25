class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for index_c, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], index_c]
            
            seen[num] = index_c