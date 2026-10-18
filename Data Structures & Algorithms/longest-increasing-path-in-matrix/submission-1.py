class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        nr, nc = len(matrix), len(matrix[0])

        def dfs(r,c): 
            if (r,c) in memo: 
                return memo[(r,c)]

            max_length = 1

            for dr, dc in directions: 
                newR, newC = r + dr, c + dc

                if 0 <= newR < nr and 0 <= newC < nc and matrix[newR][newC] > matrix[r][c]:
                    max_length = max(max_length, dfs(newR,newC) + 1)

            memo[(r,c)] = max_length
            return max_length

        return max(dfs(r, c) for r in range(nr) for c in range(nc))