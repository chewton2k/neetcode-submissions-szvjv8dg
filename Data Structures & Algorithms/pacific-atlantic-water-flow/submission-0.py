class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:   
            return []

        nr, nc = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row < 0 or row >= nr or col < 0 or col >= nc:
                        continue
                    if (row, col) in visited:
                        continue
                    if heights[row][col] < heights[r][c]:
                        continue

                    visited.add((row, col))
                    q.append((row, col))

            return visited

        pacific_starts = [(0, c) for c in range(nc)] + [(r, 0) for r in range(nr)]
        atlantic_starts = [(nr - 1, c) for c in range(nc)] + [(r, nc - 1) for r in range(nr)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return list(pacific & atlantic)
            