class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def is_safe(graph, cur, visited, terminal):

            visited[cur] = True

            for node in graph[cur]:

                if visited[node]:
                    if not terminal[node]:
                        return False
                    continue
                
                if not is_safe(graph, node, visited, terminal):
                    return False         
            
            terminal[cur] = True
            return True

        n = len(graph)
        terminal = [False] * n
        visited = [False] * n

        for node in range(n):

            if visited[node]: 
                continue

            is_safe(graph, node, visited, terminal)
        
        return [i for i in range(n) if terminal[i]]