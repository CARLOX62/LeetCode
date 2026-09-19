# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,result):
        if root == None:
            return
        self.solve(root.left,result)
        result.append(root.val)
        self.solve(root.right,result)    
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:    
        result = []
        self.solve(root,result)
        return result[k - 1]