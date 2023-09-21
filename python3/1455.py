class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        visited = set()

        roads = set()
        routes = defaultdict(list)
        for route in connections:
            routes[route[0]].append(route)
            routes[route[1]].append(route)

        def dfs(city):
            nonlocal res, roads, routes, visited
            for road in routes[city]:
                if city in road and tuple(road) not in roads:
                    roads.add(tuple(road))
                    if road[0] == city:
                        res += 1
                        if road[1] not in visited:
                            dfs(road[1])
                    else:
                        if road[0] not in visited:
                            dfs(road[0])

        dfs(0)
        
        return res
