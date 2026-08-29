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

        n = len(l1)
        left = 0
        right = n-1 
        while left <= right:
            if l1[left] != l1[right]:
                return False
            left = left + 1
            right = right - 1
        return True        