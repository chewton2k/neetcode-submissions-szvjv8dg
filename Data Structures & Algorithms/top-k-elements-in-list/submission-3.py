class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_list = Counter(nums)
        result = [key for key, _ in nums_list.most_common(k)]
        return result
            