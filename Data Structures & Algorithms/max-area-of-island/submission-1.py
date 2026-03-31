class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        nr, nc = len(grid), len(grid[0])
        q = deque()
        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    q.append((r, c))
                    current_area = 0
                    while q:
                        curr_r, curr_c = q.popleft()
                        current_area += 1
                        for dr, dc in directions:
                            nr_r, nr_c = curr_r + dr, curr_c + dc
                            if 0 <= nr_r < nr and 0 <= nr_c < nc and grid[nr_r][nr_c] == 1:
                                grid[nr_r][nr_c] = 0
                                q.append((nr_r, nr_c))
                    result = max(result, current_area)


        return result