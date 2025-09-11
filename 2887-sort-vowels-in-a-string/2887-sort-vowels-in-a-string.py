class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        s_list = list(s)

        # Step 1: Extract and store all vowels.
        for char in s_list:
            if self.is_vowel(char):
                vowels.append(char)
        
        # Step 2: Sort the vowels.
        vowels.sort()

        vowel_index = 0
        # Step 3: Replace vowels in the list with sorted vowels.
        for i in range(len(s_list)):
            if self.is_vowel(s_list[i]):
                s_list[i] = vowels[vowel_index]
                vowel_index += 1
        
        return "".join(s_list)
    
    def is_vowel(self, char: str) -> bool:
        return char.lower() in "aeiou"