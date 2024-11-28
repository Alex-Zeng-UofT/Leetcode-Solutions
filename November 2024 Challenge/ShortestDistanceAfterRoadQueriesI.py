class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        connections = {key: [key + 1] for key in range(n)}

        def find_shortest() -> int:
            
            visited = [False] * n
            count = 0
            queue, next = [0], []

            while queue:

                cur = queue.pop()
                visited[cur] = True

                for dest in connections[cur]:
                    
                    if visited[dest]: continue
                    
                    if dest == n - 1:
                        return count + 1
                    else:
                        next.append(dest)

                if not queue:
                    queue = next.copy()
                    next = []
                    count += 1
                
            return n

        ret = []

        for origin, dest in queries:
            connections[origin].append(dest)
            ret.append(find_shortest())

        return ret