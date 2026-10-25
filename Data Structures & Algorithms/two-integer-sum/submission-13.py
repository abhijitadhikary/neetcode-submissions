class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_seen = dict()

        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in dict_seen:
                return [dict_seen[diff], index]
            else:
                dict_seen[nums[index]] = index