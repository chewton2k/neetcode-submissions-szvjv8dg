class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs or dfs 
        #visited set or turn square that im on to 0
        #double for loop to call bfs or dfs when i see a 1 

        nr, nc = len(grid), len(grid[0])
        count = 0
        def dfs(r, c): 
            if r >= nr or r < 0 or c >= nc or c < 0: return 
            if grid[r][c] == "0": return 
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c - 1)
            dfs(r, c + 1)

    
        for r in range(nr): 
            for c in range(nc): 
                if grid[r][c] == "1": 
                    dfs(r,c)
                    count += 1
        
        return count 