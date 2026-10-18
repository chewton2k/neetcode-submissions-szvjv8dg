class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        q = deque()
        q.append((source, 0))
        visited = set()
        visited.add(source)
        adj = defaultdict(list)

        for i, route in enumerate(routes):
            for stop in route: 
                adj[stop].append(i)



        while q: 
            node, num_buses = q.popleft() 

            if node == target: 
                return num_buses


            for route in adj[node]: 
                for stop in routes[route]:
                    if stop not in visited: 
                        q.append((stop, num_buses + 1))
                        visited.add(stop)


        return -1

