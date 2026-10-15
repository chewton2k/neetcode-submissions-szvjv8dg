class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0 
        q = deque()
        directions = [[-1,0], [1,0],[0,1],[0,-1]]
        nr, nc = len(grid), len(grid[0])

        for r in range(nr): 
            for c in range(nc):
                if grid[r][c] == 1: 
                    q.append((r,c))
                    grid[r][c] = 0
                    current_area = 0
                    while q: 
                        row, col = q.popleft()
                        current_area += 1

                        for dr, dc in directions: 
                            newr, newc = dr + row, dc + col
                            if newr < 0 or newr >= nr or newc < 0 or newc >= nc or grid[newr][newc] == 0: 
                                continue
                            
                            grid[newr][newc] = 0
                            q.append((newr,newc))


                    
                    result = max(result, current_area)



        return result