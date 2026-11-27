class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        nums = set(nums)
        list_start_candidates = []
        to_remove = []
        
        for num in nums:
            if num-1 not in nums and num+1 in nums:
                list_start_candidates.append(num)
                to_remove.append(num)
            if num-1 not in nums and num+1 not in nums:
                to_remove.append(num)

        for num in to_remove:
            nums.remove(num)

        len_max = 1
        for num in list_start_candidates:
            len_c = 1

            while True:
                if num+1 in nums:
                    len_c += 1
                    num += 1
                else:
                    len_max = max(len_max, len_c)
                    len_c = 1
                    break
        return len_max