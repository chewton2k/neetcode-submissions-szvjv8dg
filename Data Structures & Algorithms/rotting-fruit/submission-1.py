class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        nr, nc = len(grid), len(grid[0])
        q = deque()
        directions = [[1,0], [-1,0], [0,1],[0,-1]]

        for r in range(nr):
            for c in range(nc): 
                if grid[r][c] == 1: 
                    fresh += 1

        
        for r in range(nr): 
            for c in range(nc): 
                if grid[r][c] == 2:
                    q.append((r,c))


        while q and fresh > 0: 

            for i in range(len(q)): 
                r, c = q.popleft() 
                for dr, dc in directions: 
                    row, col = dr + r, dc + c
                    if row < 0 or row >= nr or col < 0 or col >= nc: continue
                    if grid[row][col] != 1: continue 

                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1 



                    