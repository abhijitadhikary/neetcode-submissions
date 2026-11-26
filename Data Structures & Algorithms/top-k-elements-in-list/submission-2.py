class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        dict_counter = dict()

        # O(n)
        for num in nums:
            dict_counter[num] = dict_counter.get(num, 0) + 1
        
        # O(nlogn)
        dict_counter = sorted(dict_counter.items(), key=lambda item : item[1], reverse=True)
        return [i[0] for i in dict_counter[:k]]
        