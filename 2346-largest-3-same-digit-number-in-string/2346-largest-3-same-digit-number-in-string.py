class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = 999
        while nums != 0:
            if str(nums) in num:
                return str(nums)
            nums -= 111
        return "" if "000" not in num else "000"