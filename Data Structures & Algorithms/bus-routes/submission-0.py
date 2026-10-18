class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        q = deque() 
        q.append((source, 0))
        num_buses = 0
        adj = defaultdict(list)
        visited = set()
        visited.add(source)


        for i, route in enumerate(routes):
            for stop in route:
                adj[stop].append(i)



        while q: 
            stop, num_buses = q.popleft()

            if stop == target: 
                return num_buses

    

            for route in adj[stop]:
                for stp in routes[route]: 
                    if stp not in visited: 
                        q.append((stp, num_buses + 1))
                        visited.add(stp)


        return -1