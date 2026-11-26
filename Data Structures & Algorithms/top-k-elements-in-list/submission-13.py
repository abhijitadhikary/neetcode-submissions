import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict_freq = Counter(nums)
        list_bucket = [[] for _ in range(max(dict_freq.values()) + 1)]

        for key, freq in dict_freq.items():
            list_bucket[freq] += [key]
        
        list_return = []
        for idx_rev in range(len(list_bucket)-1, -1, -1):
            for item in list_bucket[idx_rev]:
                list_return.append(item)
                if len(list_return) == k:
                    return list_return
        






        # dict_freq = Counter(nums)
        # min_heap = []
        # for num, freq in dict_freq.items():
        #     if len(min_heap) < k:
        #         heapq.heappush(min_heap, (freq, num))
        #     elif min_heap[0][0] < freq:
        #         heapq.heapreplace(min_heap, (freq, num))
        # return [num for freq, num in min_heap]
        

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
        