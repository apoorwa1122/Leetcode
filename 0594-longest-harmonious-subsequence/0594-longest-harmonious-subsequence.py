class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d=Counter(nums)
        m=0
        for i in nums:
            if d[i+1]>0:
                m=max(m,d[i]+d[i+1])
        return m