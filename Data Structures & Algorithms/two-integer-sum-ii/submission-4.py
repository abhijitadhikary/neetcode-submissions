class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(nums, t, idx_l, idx_r):
            if idx_l == idx_r:
                if nums[idx_l] != t:
                    return False
            idx_mid = (idx_l+idx_r)//2
            val_mid = nums[idx_mid]
            if val_mid == t:
                return idx_mid
            elif val_mid > t:
                return binary_search(nums, t, idx_l, idx_mid)
            else:
                return binary_search(nums, t, idx_mid+1, idx_r)
        
        for idx in range(len(numbers)-1):
            diff = target - numbers[idx]
            idx_2 = binary_search(numbers, diff, idx+1, len(numbers)-1)
            if idx_2:
                return [idx+1, idx_2+1]

        return binary_search(numbers, target, 0, len(numbers)-1)