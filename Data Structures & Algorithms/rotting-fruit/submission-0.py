
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result_mins = 0
        rotting = deque() 
        fresh = 0
        c = len(grid)
        r = len(grid[0])


        for nc in range(c): 
            for nr in range(r): 
                if grid[nc][nr] == 2: 
                    rotting.append([nc, nr])


        for nc in range(c): 
            for nr in range(r): 
                if grid[nc][nr] == 1: 
                    fresh += 1
        


        while rotting and fresh > 0:
            for _ in range(len(rotting)):
                curr_r, curr_c = rotting.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc 
                    if 0 <= nr < c and 0 <= nc < r and grid[nr][nc] == 1:                      
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotting.append((nr, nc))
            result_mins += 1


        return result_mins if fresh == 0 else -1

