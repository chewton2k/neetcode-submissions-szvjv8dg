class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for cnt, num in enumerate(nums): 
            look = target - num

            if look in seen: 
                return [seen[look], cnt]

            seen[num] = cnt 

        return []