class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0

        # On parcourt chaque lettre possible 'a' à 'z'
        for c in "abcdefghijklmnopqrstuvwxyz":
            first = s.find(c)
            last = s.rfind(c)

            # Il faut au moins deux occurrences pour former un palindrome de type a_x_a
            if first != -1 and first < last:
                # Ensemble des lettres entre la première et la dernière occurrence
                middle_chars = set(s[first + 1 : last])
                # Chaque caractère du milieu forme un palindrome unique
                result += len(middle_chars)

        return result