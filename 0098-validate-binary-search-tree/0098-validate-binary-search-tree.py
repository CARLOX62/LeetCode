# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,limit):
        if root is None:
            return True
        if not limit[0] < root.val < limit[1]:
            return False   
        left = self.solve(root.left,[limit[0],root.val])
        if left == False:
            return False
        right = self.solve(root.right,[root.val,limit[1]])   
        return left and right

    def isValidBST(self, root: TreeNode | None) -> bool:

        return self.solve(root,[float("-inf"),float("inf")])