class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = {(a, b) for a, b in connections}
        neighbours = {k: [] for k in range(n)}
        visited = [False for i in range(n)]
        
        for edge in edges:
            a, b = edge
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        ret = 0

        def dfs(city: int) -> None:
            nonlocal edges, neighbours, visited, ret
            
            for neighbour in neighbours[city]:
                
                if not visited[neighbour]:
                    if (neighbour, city) not in edges:
                        ret += 1

                    visited[neighbour] = True
                    dfs(neighbour)
            return

        visited[0] = True
        dfs(0)

        return ret