
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []
        heap = [(-count, num) for num, count in freq.items()]
        heapify(heap)

        for _ in range(k): 
            result.append(heappop(heap)[1])


        return result
            