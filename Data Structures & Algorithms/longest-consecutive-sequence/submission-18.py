class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        elif len(nums) == 2:
            if abs(nums[1]-nums[0])==1:
                return 2
            else:
                return 1

        dict_len = dict()
        len_max = 0

        for num in nums:
            if num not in dict_len:
                len_left = dict_len.get(num-1, 0)
                len_right = dict_len.get(num+1, 0)
                len_c = len_left + 1 + len_right

                dict_len[num] = len_c
                dict_len[num-len_left] = len_c
                dict_len[num+len_right] = len_c
                
                len_max = max(len_max, len_c)
        return len_max



        