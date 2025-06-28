class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [info[0] for info in sorted(sorted([(x, i) for i, x in enumerate(nums)], reverse=True)[:k], key=lambda info: info[1])]
        