# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Middle element
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse The Second Part
        prev = None
        curr = slow
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        # Add

        first = head
        second = prev
        maxi = 0

        while second is not None:
            total = first.val + second.val
            maxi = max(maxi,total)
            first = first.next
            second = second.next
        return maxi    


