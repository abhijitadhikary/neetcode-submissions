import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count = dict()
        for num in nums:
            dict_count[num] = dict_count.get(num, 0) + 1
        
        tuple_count = [(v, k)for (k, v) in dict_count.items()]
        
        heapq._heapify_max(tuple_count)
        
        list_top_k = []
        for index in range(k):
            v, k = heapq._heappop_max(tuple_count)
            list_top_k.append(k)
        return list_top_k
        