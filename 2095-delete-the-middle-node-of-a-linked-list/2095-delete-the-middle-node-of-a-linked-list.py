# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None
        
        low = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = low
            low = low.next
            fast = fast.next.next
        prev.next  = low.next            
        return head
            



        