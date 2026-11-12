# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        low = head
        fast = head
        while fast is not None and fast.next is not None:
            low = low.next
            fast = fast.next.next
        return low
        