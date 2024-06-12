# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        mid = head 
        fast = head

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        cur = mid
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        ret = 0
        sec_head = prev

        while sec_head:
            ret = max(ret, head.val + sec_head.val)
            head = head.next
            sec_head = sec_head.next

        return ret
        