class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        Count unique 3-letter palindromic subsequences
        Strategy: Find first/last occurrence + count unique middles
        
        :type s: str - input string of lowercase letters
        :rtype: int - count of unique palindromic subsequences
        """
        
        # 🎯 Step 1: Initialize result counter
        r = 0  # Total count of palindromic subsequences
        
        # 📊 Step 2: Track processed characters (avoid duplicates)
        seen = set()  # Characters we've already analyzed
        
        # 🔄 Step 3: Process each character in the string
        for i in range(len(s)):
            
            # ✅ Skip if we've already processed this character
            if s[i] not in seen:
                
                # 🎪 Step 4: Find first occurrence (current position)
                start = i
                last = i  # Initialize last to start
                
                # 🔍 Step 5: Find LAST occurrence of this character
                # This defines the "span" for palindromes XYX
                for j in range(i + 1, len(s)):
                    if s[j] == s[i]:
                        last = j  # Update last occurrence
                
                # 🌟 Step 6: Extract characters BETWEEN first and last
                # These are potential middle characters for palindromes
                check = set(s[start + 1:last])
                
                # 💡 Step 7: Count unique middle characters
                # Each unique char forms one palindrome: X + char + X
                c = len(check)
                r += c  # Add to total count
                
                # ✓ Step 8: Mark this character as processed
                seen.add(s[i])
        
        # 🎉 Return total count of unique palindromic subsequences
        return r


# 🎓 Algorithm Walkthrough Example:
#
# Input: s = "aabca"
#
# Step 1: INITIALIZE
# r = 0 (result counter)
# seen = {} (empty set)
#
# Step 2: PROCESS i=0, char='a'
# 'a' not in seen → Process it!
#   start = 0
#   Find last 'a': j=1 ('a'), j=2 ('b'), j=3 ('c'), j=4 ('a') → last = 4
#   Middle substring: s[1:4] = "abc"
#   Unique middles: {'a', 'b', 'c'} → count = 3
#   Palindromes: "aaa", "aba", "aca" ✅
#   r = 0 + 3 = 3
#   seen = {'a'}
#
# Step 3: PROCESS i=1, char='a'  
# 'a' in seen → Skip! ✓
#
# Step 4: PROCESS i=2, char='b'
# 'b' not in seen → Process it!
#   start = 2, last = 2 (no other 'b')
#   Middle substring: s[3:2] = "" (empty)
#   Unique middles: {} → count = 0
#   r = 3 + 0 = 3
#   seen = {'a', 'b'}
#
# Step 5: PROCESS i=3, char='c'
# 'c' not in seen → Process it!
#   start = 3, last = 3 (no other 'c')
#   Middle substring: s[4:3] = "" (empty)
#   Unique middles: {} → count = 0
#   r = 3 + 0 = 3
#   seen = {'a', 'b', 'c'}
#
# Step 6: PROCESS i=4, char='a'
# 'a' in seen → Skip! ✓
#
# Result: r = 3 🎉
#
# 🔑 Why This Works:
#
# 1. **First/Last Span:** Defines outer chars of palindrome XYX
# 2. **Unique Middles:** Set ensures we count each palindrome once
# 3. **Seen Tracking:** Prevents reprocessing same character
# 4. **Subsequence Property:** Characters don't need to be consecutive!
#
# 🚀 Key Insights:
# - Only need first and last occurrence of each character
# - Middle character can be ANYTHING between them
# - Set automatically handles uniqueness
# - Each character processed exactly once
#
# 🎯 Time: O(n²), Space: O(1) constant ⚡