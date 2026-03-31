class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = Counter(nums)

        for m, n in num.items(): 
            if n > 1: 
                return m

        return -1