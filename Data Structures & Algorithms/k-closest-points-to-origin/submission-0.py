from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heap.append([distance, [x, y]])

        heapq.heapify(heap)

        for i in range(k): 
            result.append(heapq.heappop(heap)[1])

    
        return result
