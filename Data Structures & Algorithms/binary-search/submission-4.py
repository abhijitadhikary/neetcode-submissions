class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index_low = 0
        index_high = len(nums) - 1
        
        while True:
            index_mid = int((index_low + index_high) / 2)
            val_mid = nums[index_mid]
            if target == val_mid:
                return index_mid
            else:
                if target < val_mid:
                    index_high = index_mid - 1
                else:
                    index_low = index_mid + 1
                if index_high < index_low:
                    return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     return self._search(nums, target, 0, len(nums)-1)
        
    # def _search(self, nums, target, index_low, index_high):
    #     if index_high < index_low:
    #         return -1
    #     else:
    #         index_mid = int((index_low + index_high) / 2)
    #         val_mid = nums[index_mid]
    #         if target == val_mid:
    #             return index_mid
    #         elif target < val_mid:
    #             return self._search(nums, target, index_low, index_mid-1)
    #         else:
    #             return self._search(nums, target, index_mid+1, index_high)
