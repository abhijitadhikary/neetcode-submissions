class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        len_max = 0
        for num in nums:
            if num-1 not in nums:
                len_c = 1

                while True:
                    if num+1 in nums:
                        len_c += 1
                        num += 1
                    else:
                        len_max = max(len_max, len_c)
                        len_c = 1
                        break
        return len_max