class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        
        for i, j in enumerate(nums):
            num = target - j
            if num in visited: 
                return [visited[num], i]
            visited[j] = i
            # if num not in visited: 
            #     visited[j] = i

            # return [i, visited[num]]


        return [ ]
