class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []

        for num, c in count.items(): 
            result.append((num, c))


        result.sort(key = lambda x:x[1], reverse = True)
        
        return [res[0] for res in result[:k]]