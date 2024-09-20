class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}
        ret = []

        for i, pair in enumerate(equations):
            if pair[0] not in graph:
                graph[pair[0]] = {pair[1]: values[i]}
            else: graph[pair[0]][pair[1]] = values[i]

            if pair[1] not in graph:
                graph[pair[1]] = {pair[0]: 1/float(values[i])}
            else: graph[pair[1]][pair[0]] = 1/float(values[i])
        
        for query in queries: 
            ret.append(self.dfs(graph, query[0], query[1], 1, []))

        return ret

    def dfs(self, graph: dict, cur: str, target: str, val: float, visited: List) -> float:

        if cur not in graph: return -1
        if cur == target: return 1

        visited.append(cur)
        
        for key in graph[cur]:

            if key in visited: continue

            temp = val * graph[cur][key]

            if key == target: return temp

            visited.append(key)

            res = self.dfs(graph, key, target, temp, visited)
            
            if res != -1:
                return res

        return -1
            
        