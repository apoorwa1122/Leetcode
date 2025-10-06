import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Min-heap: (max_elevation_so_far, r, c)
        pq = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while pq:
            elev, r, c = heapq.heappop(pq)
            if r == n - 1 and c == n - 1:
                return elev
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The elevation to enter this cell is max(elev, grid[nr][nc])
                    heapq.heappush(pq, (max(elev, grid[nr][nc]), nr, nc))
        
        return -1  # Should not happen