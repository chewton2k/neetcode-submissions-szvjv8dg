class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0 

        for num in nums: 
            if num - 1 not in seen: 
                current_num = num
                count = 1
                while current_num + 1 in seen: 
                    current_num += 1
                    count +=1

                result = max(result, count)


        return result
                