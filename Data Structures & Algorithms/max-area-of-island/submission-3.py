class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0 
        nr, nc = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        q = deque()

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
                            new_row, new_col = row + dr, col + dc
                            if new_row < 0 or new_row >= nr or new_col < 0 or new_col >= nc or grid[new_row][new_col] == 0: 
                                continue

                            grid[new_row][new_col] = 0
                            q.append((new_row, new_col))

                    result = max(result, current_area)


        return result 