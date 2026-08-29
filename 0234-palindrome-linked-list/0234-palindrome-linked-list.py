# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = []
        curr = head
        while curr is not None:
            l1.append(curr.val)
            curr = curr.next
        return l1 == l1[::-1]       