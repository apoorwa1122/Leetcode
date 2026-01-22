class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        res = 0
        while any(starmap(gt,pairwise(a))):
            res,q,i = res+1,*min(zip(map(sum,pairwise(a)),count()))
            a = a[:i]+[q]+a[i+2:]
            
        return res