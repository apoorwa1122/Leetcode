class Solution:
    def maximumDifference(self, nums):
        ans = -1
        mini = nums[0]
        for i in range(1, len(nums)):
            mini = min(mini, nums[i])
            if nums[i] > mini:
                ans = max(ans, nums[i] - mini)
        return ans