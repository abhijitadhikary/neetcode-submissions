class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx_l = 0
        idx_r = len(numbers)-1

        while idx_l < idx_r:
            diff = target - (numbers[idx_l] + numbers[idx_r])
            if diff == 0:
                return [idx_l+1, idx_r+1]
            elif diff > 0:
                idx_l += 1
            else:
                idx_r -= 1