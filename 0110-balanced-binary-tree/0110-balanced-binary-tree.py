# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root == None:
            return 0
        LH = self.solve(root.left)
        if LH == -1:
            return -1
        RH = self.solve(root.right)
        if RH == -1:
            return -1
        if abs(RH - LH) > 1:
            return -1    
        return 1 + max(LH,RH)            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x = self.solve(root)
        if x == -1:
            return False
        return True    