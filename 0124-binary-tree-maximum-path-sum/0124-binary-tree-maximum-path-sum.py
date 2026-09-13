# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float('-inf')
    def solve(self,root):
        if root == None:
            return 0
        LS = self.solve(root.left)
        if LS < 0:
            LS = 0
        RS = self.solve(root.right)
        if RS < 0:
            RS = 0
        self.maxi = max(self.maxi,LS + root.val + RS)
        return max(LS,RS) + root.val            
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.maxi