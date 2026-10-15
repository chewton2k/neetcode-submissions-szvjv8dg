class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = [[] for i in range(len(nums) + 1)] 

        for num, i in count.items(): 
            result[i].append(num)

        res = []
        for i in range(len(result) -1, -1, -1):
            for num in result[i]:
                if result and k > 0: 
                    res.append(num)
                    k -= 1

        
        return res