class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_result, zero_count = 1, 0
        n = len(nums) 
        for num in nums: 
            if num: 
                product_result *= num
            else: 
                zero_count += 1
        
        if zero_count > 1: 
            return [0] * n

        result = [0] * n
        for i, c in enumerate(nums): 
            if zero_count: 
                result[i] = 0 if c else product_result 
            else: 
                result[i] = product_result // c
        return result 
            
