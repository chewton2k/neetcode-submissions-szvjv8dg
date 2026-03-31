class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs or dfs 
        #visited set or turn square that im on to 0
        #double for loop to call bfs or dfs when i see a 1 
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        nr, nc = len(grid), len(grid[0])
        count = 0
        def bfs(r,c): 
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q: 
                row, col = q.popleft()
                for dr, dc in directions:
                    newr, newc = dr + row, dc + col
                    if (newr < 0 or newc < 0 or newr >=nr or newc>=nc or grid[newr][newc] == "0"): continue
                    q.append((newr,newc))
                    grid[newr][newc] = "0" 



    
        for r in range(nr): 
            for c in range(nc): 
                if grid[r][c] == "1": 
                    bfs(r,c)
                    count += 1
        
        return count 