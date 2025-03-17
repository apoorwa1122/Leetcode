class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return reduce(operator.xor, [1<<x for x in nums], 0)==0
        