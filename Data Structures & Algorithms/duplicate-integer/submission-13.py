class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        found = set()
        for num in nums:
            if num not in found:
                found.add(num)
            else:
                return True
        return False

        # # brute force
        # n = len(nums)
        # for index_a in range(n):
        #     num_c = nums[index_a]
        #     for index_b in range(index_a+1, n):
        #         if num_c == nums[index_b]:
        #             return True
        # return False