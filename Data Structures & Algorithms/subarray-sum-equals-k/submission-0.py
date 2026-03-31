class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = currSum = 0

        prefix = {0: 1} 

        for num in nums: 
            currSum += num
            diff = currSum - k
            if diff in prefix:  
                result += prefix[diff]
            
            if currSum in prefix:
                prefix[currSum] += 1
            else:
                prefix[currSum] = 1

        return result