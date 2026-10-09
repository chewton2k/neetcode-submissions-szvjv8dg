class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set() 
        n = len(isConnected)
        res = 0

        def dfs(city): 
            visited.add(city)
            for neighbor in range(n): 
                if isConnected[city][neighbor] == 1 and neighbor not in visited: 
                    dfs(neighbor)

        for i in range(n): 
            if i not in visited: 
                dfs(i)
                res += 1

        
        return res
