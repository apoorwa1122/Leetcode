class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n  # Initialize the result array with zeros
        
        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                # Calculate the target index using modular arithmetic
                target_index = (i + nums[i]) % n
                # Handle negative indices by wrapping around the end of the array
                if target_index < 0:
                    target_index += n
                result[i] = nums[target_index]
        
        return result

# Example usage
nums1 = [3, -2, 1, 1]
print(Solution().constructTransformedArray(nums1))  # Output: [1, 1, 1, 3]

nums2 = [-1, 4, -1]
print(Solution().constructTransformedArray(nums2))  # Output: [-1, -1, 4]
