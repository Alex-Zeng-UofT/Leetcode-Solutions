# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        cur = head
        
        while cur:
            
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev
            
        