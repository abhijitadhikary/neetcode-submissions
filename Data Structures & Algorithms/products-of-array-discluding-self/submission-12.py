class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_prefix = [1]
        list_postfix = [1]

        for idx in range(1, len(nums)):
            list_prefix.append(list_prefix[idx-1] * nums[idx-1])
            list_postfix.append(list_postfix[idx-1] * nums[len(nums)-idx])
        
        list_return = []
        for idx in range(len(nums)):
            list_return.append(list_prefix[idx]*list_postfix[len(nums)-1-idx])
        
        return list_return


        