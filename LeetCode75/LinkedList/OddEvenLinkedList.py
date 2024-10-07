# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None

        odd_head = head
        even_head = head.next

        odd = odd_head
        even = even_head

        while odd and odd.next and even and even.next:

            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = even_head

        return odd_head

        