class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # attempt 3: prefix mults

        prefix_mult_lr = [1]
        prefix_mult_rl = [1]
        n = len(nums)

        for idx in range(n):
            prefix_mult_lr.append(prefix_mult_lr[-1] * nums[idx])
            prefix_mult_rl.append(prefix_mult_rl[-1] * nums[n - idx - 1])
        
        prods = []
        for idx in range(n):
            prods.append(prefix_mult_lr[idx]*prefix_mult_rl[n-idx-1])
        return prods