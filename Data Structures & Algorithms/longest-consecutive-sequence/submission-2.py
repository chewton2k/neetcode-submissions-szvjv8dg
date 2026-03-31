class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        longest_consecutive = 0 

        for num in nums: 
            if num - 1 not in count: 
                current_num = num 
                current_streak = 1
                while current_num + 1 in count: 
                    current_streak += 1
                    current_num += 1
                longest_consecutive = max(longest_consecutive, current_streak)


        return longest_consecutive
                