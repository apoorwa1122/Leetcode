class Solution:
    def partitionArray(self, nums, k):
        nums.sort()  # Sort the numbers
        count = 1    # At least one group is needed
        start = nums[0]  # First number in the first group

        for num in nums:
            if num - start > k:
                count += 1    # New group needed
                start = num   # Start of new group

        return count
