import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count = Counter(nums)
        
        tuple_count = [(v, k)for (k, v) in dict_count.items()]
        
        heapq._heapify_max(tuple_count)
        
        list_top_k = []
        for index in range(k):
            v, k = heapq._heappop_max(tuple_count)
            list_top_k.append(k)
        return list_top_k

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # O(n)
    #     items_unique = set(nums)
    #     dict_counter = dict()

    #     # O(n)
    #     for num in nums:
    #         dict_counter[num] = dict_counter.get(num, 0) + 1
        
    #     dict_counter = sorted(dict_counter.items(), key=lambda item : item[1], reverse=True)
    #     return [i[0] for i in dict_counter[:k]]
        