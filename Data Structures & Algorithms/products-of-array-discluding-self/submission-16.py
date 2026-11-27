class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_prefix = [1] * len(nums)
        list_postfix = [1] * len(nums)

        for idx in range(1, len(nums)):
            list_prefix[idx] = list_prefix[idx-1] * nums[idx-1]
            list_postfix[len(nums)-1-idx] = list_postfix[len(nums)-idx] * nums[len(nums)-idx]
        
        return [list_prefix[idx]*list_postfix[idx] for idx in range(len(nums))]