class Solution:
    def maximumUniqueSubarray(self, nums):
        basket = set()
        max_score = 0
        current_score = 0
        start = 0

        for end in range(len(nums)):
            while nums[end] in basket:
                basket.remove(nums[start])
                current_score -= nums[start]
                start += 1
            basket.add(nums[end])
            current_score += nums[end]
            max_score = max(max_score, current_score)

        return max_score
