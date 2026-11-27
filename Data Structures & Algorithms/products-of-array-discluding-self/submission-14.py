class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_prefix = [1 for _ in range(len(nums))]
        list_postfix = [1 for _ in range(len(nums))]

        for idx in range(1, len(nums)):
            list_prefix[idx] = list_prefix[idx-1] * nums[idx-1]
            list_postfix[len(nums)-idx-1] = list_postfix[len(nums)-idx] * nums[len(nums)-idx]

        list_return = [list_prefix[index] * list_postfix[index] for index in range(len(nums))]
        
        return list_return


        