class Solution:
    def solve(self, n, curr):
        if n == 0: return True
        if n < 0 or curr < 0: return False
        take = n - math.pow(3, curr)
        return self.solve(take, curr - 1) or self.solve(n, curr - 1)
    
    def checkPowersOfThree(self, n: int) -> bool:
        maxPow = floor(math.log(n)/math.log(3))
        return self.solve(n, maxPow)