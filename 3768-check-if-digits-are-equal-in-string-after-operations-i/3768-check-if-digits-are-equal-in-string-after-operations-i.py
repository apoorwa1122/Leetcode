class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(c) for c in s]
        
        # Keep performing operations until only 2 digits remain
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = new_digits
        
        # Return whether final two digits are equal
        return digits[0] == digits[1]
