# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        temp = head
        for _ in range(1,count//2):
            temp = temp.next
        temp.next = temp.next.next
        return head    

