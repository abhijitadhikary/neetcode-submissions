class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_prod_prefix = [1]
        arr_prod_postfix = [1]

        l = len(nums)
        for idx in range(1, l):

            arr_prod_prefix.append(arr_prod_prefix[idx-1] * nums[idx-1])
            arr_prod_postfix.append(arr_prod_postfix[idx-1] * nums[l-idx])
            

        list_return = []
        for idx in range(l):
            list_return.append(arr_prod_prefix[idx] * arr_prod_postfix[l-idx-1])
        return list_return


        