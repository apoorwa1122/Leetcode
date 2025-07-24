class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        subxor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        par = [-1] * n
        time = [0]

        def dfs(u, p):
            in_time[u] = time[0]
            time[0] += 1
            subxor[u] = nums[u]
            par[u] = p
            for v in g[u]:
                if v != p:
                    dfs(v, u)
                    subxor[u] ^= subxor[v]
            out_time[u] = time[0]
            time[0] += 1

        dfs(0, -1)
        total = subxor[0]
        ans = float('inf')

        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    continue

                if is_ancestor(i, j):
                    x = subxor[j]
                    y = subxor[i] ^ subxor[j]
                    z = total ^ subxor[i]
                elif is_ancestor(j, i):
                    x = subxor[i]
                    y = subxor[j] ^ subxor[i]
                    z = total ^ subxor[j]
                else:
                    x = subxor[i]
                    y = subxor[j]
                    z = total ^ x ^ y

                mx = max(x, y, z)
                mn = min(x, y, z)
                ans = min(ans, mx - mn)

        return ans