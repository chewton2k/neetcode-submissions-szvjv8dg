class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        total = 1
        zero_count = 0

        for num in nums:
            if num != 0:  
                total *= num
            if num == 0: 
                zero_count += 1
            if zero_count >= 2: 
                return [0] * len(nums) 


        for i in range(len(nums)):

            if zero_count == 1:
                if nums[i] == 0:
                    result[i] = total
                else:
                    result[i] = 0
            else:
                result[i] = total // nums[i]



        return result