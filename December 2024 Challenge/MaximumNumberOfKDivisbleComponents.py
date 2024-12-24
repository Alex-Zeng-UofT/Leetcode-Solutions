class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        adj_list = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        component_count = [0]

        self.dfs(0, -1, adj_list, values, k, component_count)

        return component_count[0]

    def dfs(
        self,
        current_node: int,
        parent_node: int,
        adj_list: List[List[int]],
        node_values: List[int],
        k: int,
        component_count: List[int],
    ) -> int:

        sum_ = 0

        for neighbor_node in adj_list[current_node]:
            if neighbor_node != parent_node:
                sum_ += self.dfs(
                    neighbor_node,
                    current_node,
                    adj_list,
                    node_values,
                    k,
                    component_count,
                )
                sum_ %= k

        sum_ += node_values[current_node]
        sum_ %= k

        if sum_ == 0:
            component_count[0] += 1

        return sum_