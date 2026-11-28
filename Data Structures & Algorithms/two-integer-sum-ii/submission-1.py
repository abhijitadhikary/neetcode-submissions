class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, num in enumerate(numbers):
            if num in seen:
                return [seen[num]+1, idx+1]
            seen[target-num] = idx