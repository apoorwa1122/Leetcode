class Solution:
    def getDecimalValue(self, head: Optional[ListNode], ans=0) -> int:
        return self.getDecimalValue(head.next, (ans<<1)+head.val) if head else ans
        