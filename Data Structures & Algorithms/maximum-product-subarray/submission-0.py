class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]

        for i in range(len(nums)): 
            curr = nums[i]
            result = max(result, curr)

            for j in range(i + 1, len(nums)): 
                curr *= nums[j]
                result = max(result, curr)


        return result

