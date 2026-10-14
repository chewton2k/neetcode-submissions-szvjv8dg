class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        nr, nc = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        def bfs(r,c): 
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q: 
                row, col = q.popleft()

                for dr, dc in directions: 
                    newr, newc = row + dr, col + dc
                    if newr < 0 or newr >= nr or newc < 0 or newc >= nc or grid[newr][newc] == "0": continue

                    q.append((newr,newc))
                    grid[newr][newc] = "0"


        for r in range(nr): 
            for c in range(nc): 
                if grid[r][c] == "1": 
                    bfs(r,c)
                    result += 1 

        return result
