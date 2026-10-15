class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        res = count.most_common(k)


        return [r[0] for r in res]
