class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for idx_c, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                a = idx_c
                b = -1
                for idx_p in range(idx_c):
                    if nums[idx_p] == diff:
                        b = idx_p
                        break
                return [b, a]
            else:
                seen.add(num)