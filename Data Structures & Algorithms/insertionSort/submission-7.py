# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        return_list = []
        length = len(pairs)

        if length >= 0 and length <= 100:

            if length == 0:
                return []

            for index_pivot in range(1, length, 1):
                return_list.append(pairs[:])
                for index_l in range(0, index_pivot, 1):
                    if pairs[index_pivot].key < pairs[index_l].key:
                        temp = pairs[index_pivot]
                        for index_move in range(index_pivot, index_l, -1):
                            pairs[index_move] = pairs[index_move-1]
                        pairs[index_l] = temp
                        break

            return_list.append(pairs[:])

            return return_list