class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        visited = [0] * len(graph)
   
        def has_cycle(node):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False
            visited[node] = -1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            visited[node] = 1
            return False

        return [node for node in range(len(graph)) if not has_cycle(node)]