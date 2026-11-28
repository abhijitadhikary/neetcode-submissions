class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twosum(arr, target, idx_start):
            found_set = set()
            dict_seen = dict()
            for idx in range(idx_start, len(arr)):
                if arr[idx] in dict_seen:
                    found_set.add((dict_seen[arr[idx]], idx))
                else:
                    dict_seen[target-arr[idx]] = idx
            return found_set
        set_candidates = set()
        for idx_1 in range(len(nums)):
            idx_2 = idx_1+1
            found_set = twosum(nums, -nums[idx_1], idx_2)
            if found_set:
                for found_tuple in found_set:
                    candidate = tuple(sorted([nums[idx_1], nums[found_tuple[0]], nums[found_tuple[1]]]))
                    set_candidates.add(candidate)
        return [list(tup) for tup in set_candidates]