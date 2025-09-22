class Solution:
    from collections import Counter
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums=Counter(nums)
        max1=max(nums.values())
        res=0
        for v in nums.values():
            if v==max1:res+=max1
        return res