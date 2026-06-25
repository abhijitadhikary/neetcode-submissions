class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # attempt 2: using brute force left and right prods
        prods = []
        for idx_p in range(len(nums)):
            prod_c = 1
            for idx_iter in range(len(nums)):
                if idx_iter != idx_p:
                    prod_c *= nums[idx_iter]
            prods.append(prod_c)
        return prods