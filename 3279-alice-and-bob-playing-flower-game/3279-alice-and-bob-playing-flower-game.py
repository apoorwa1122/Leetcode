class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Count odd/even in [1..n] and [1..m]
        odd_n = (n + 1) // 2
        even_n = n // 2
        odd_m = (m + 1) // 2
        even_m = m // 2
        # Alice wins when x+y is odd: odd_x*even_y + even_x*odd_y
        return odd_n * even_m + even_n * odd_m

# Example local tests
if __name__ == "__main__":
    print(Solution().flowerGame(3, 2))  # 3
    print(Solution().flowerGame(1, 1))  # 0
