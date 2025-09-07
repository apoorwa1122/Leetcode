class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Generate numbers from 1 to n//2
        result = [i for i in range(1, n // 2 + 1)] + [-i for i in range(1, n // 2 + 1)]
        
        # If n is odd, add 0 in the middle
        if n % 2 != 0:
            result.append(0)
        
        return result