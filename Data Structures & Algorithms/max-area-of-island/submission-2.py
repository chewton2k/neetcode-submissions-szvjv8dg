class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0 
        nr, nc = len(grid), len(grid[0])


        def dfs(r, c):
            if r<0 or r>=nr or c<0 or c>=nc:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1,c) + dfs(r - 1,c) + dfs(r,c + 1) + dfs(r,c - 1)


        for i in range(nr): 
            for j in range(nc): 
                if grid[i][j] == 1: 
                    result = max(dfs(i,j), result)


        return result 