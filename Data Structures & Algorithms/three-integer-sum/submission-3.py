class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for i in range(len(nums)):
            seen = set() 
            for j in range(i + 1, len(nums)): 
                complement = -nums[i] - nums[j]
                if complement in seen: 
                    result.add(tuple([complement, nums[i], nums[j]]))
                seen.add(nums[j])


        return [list(i) for i in result]



        # for i in range(len(nums)): 
            # complement = target - nums[i]
            # if nums in seen: return indices
            # put complement in seen 

        