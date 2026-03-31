class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5(m), 1, 2]
        # m >= 3 search the right 
        # else search the left 

        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r: 
            if nums[l] < nums[r]: 
                return min(res, nums[l]) #[3, 1, 2] l > r [1, 2, 3] l < r 

            m = (r + l) // 2 
            res = min(res, nums[m])
            if nums[m] >= nums[l]: 
                l = m + 1
            else: 
                r = m - 1

        return res            