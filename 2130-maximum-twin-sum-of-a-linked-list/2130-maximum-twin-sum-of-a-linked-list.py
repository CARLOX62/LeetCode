# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = []
        temp = head
        while temp is not None:
            result.append(temp.val)
            temp = temp.next
        i = 0
        j = len(result) - 1
        maxi = 0
        while i < j:
            total = result[i] + result[j] 
            i += 1
            j -= 1
            maxi = max(total,maxi)
        return maxi       