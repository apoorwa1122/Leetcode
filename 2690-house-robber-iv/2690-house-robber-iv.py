class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def steal(mid):
            count= 0
            i =0
            while i<len(nums):
                if nums[i]<=mid:
                    count+=1
                    i+=2
                else:
                    i+=1
            return count>=k
        l, r = min(nums), max(nums)
        while l<r:
            m=l+(r-l)//2
            if steal(m): r=m
            else: l=m+1
        return l