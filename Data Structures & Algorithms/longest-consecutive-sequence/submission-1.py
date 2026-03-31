class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 
        seen = set(nums)

        for num in seen: 
            if num - 1 not in seen: 
                current_counter = 1 
                current_num = num
                while current_num + 1 in seen: 
                    current_num +=1
                    current_counter +=1
                count = max(count, current_counter)


        return count