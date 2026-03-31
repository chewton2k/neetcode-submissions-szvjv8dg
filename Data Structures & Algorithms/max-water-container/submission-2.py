class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #initialize two pointers one at the beginnign and one at the end
        l, r = 0, len(heights) -1 
        #we can loop while l < r 
        max_area = 0
        while l < r: 
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(area, max_area)
        #calculate the area of each of the containers in between the pointers 
            if heights[l] <= heights[r]: 
                l += 1
            elif heights[r] <= heights[l]: 
                r -= 1 

        #keep track of our max area so far and return 
        return max_area     
  