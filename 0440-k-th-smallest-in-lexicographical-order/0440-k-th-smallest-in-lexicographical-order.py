class Solution:
    def count(self, n: int, a: int, b: int) -> int:
        total = 0
        while a <= n:
            total += min(n + 1, b) - a
            a *= 10
            b *= 10
        return total

    def findKthNumber(self, n: int, k: int) -> int:
        res = 1
        k -= 1
        while k:
            steps = self.count(n, res, res + 1)
            if steps <= k:
                k -= steps
                res += 1
            else:
                res *= 10
                k -= 1
        return res