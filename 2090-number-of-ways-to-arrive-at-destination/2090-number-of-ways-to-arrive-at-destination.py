class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, t in roads:
            adj[u].append((t, v))
            adj[v].append((t, u))
        dist = [(0, 0, -1)] # time, node, previous
        vis = set()
        ways = [0] * (n + 1) # ways to reach each node
        ways[-1] = 1
        while dist:
            time, node, prev = heappop(dist)
            if node in vis:
                continue
            vis.add(node)
            ways[node] += ways[prev]
            while dist and dist[0][0] == time and dist[0][1] == node: # while time to reach current node is lowest we add ways to reach it
                _, _, p = heappop(dist)
                ways[node] += ways[p]
            if node == n-1:
                return ways[node] % (10 ** 9 + 7)
            for t, nd in adj[node]:
                if nd not in vis:
                    heappush(dist, (t + time, nd, node))

            