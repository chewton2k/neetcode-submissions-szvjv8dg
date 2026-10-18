class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)

        for key, value in count.items(): 
            freq[value].append(key)

        res = []
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                if freq and k > 0: 
                    res.append(num)
                    k -= 1

        return res