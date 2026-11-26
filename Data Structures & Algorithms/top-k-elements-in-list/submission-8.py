import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_frequency = Counter(nums)

        min_heap = []

        for num, freq in dict_frequency.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]


    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # O(n), u unique
    #     dict_count = Counter(nums)
        
    #     # O(u)
    #     tuple_count = [(-v, k) for (k, v) in dict_count.items()]
        
    #     # O(u)
    #     heapq.heapify(tuple_count)
        
    #     # O(k log u)
    #     return [heapq.heappop(tuple_count)[1] for _ in range(k)]

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # O(n)
    #     items_unique = set(nums)
    #     dict_counter = dict()

    #     # O(n)
    #     for num in nums:
    #         dict_counter[num] = dict_counter.get(num, 0) + 1
        
    #     dict_counter = sorted(dict_counter.items(), key=lambda item : item[1], reverse=True)
    #     return [i[0] for i in dict_counter[:k]]
        