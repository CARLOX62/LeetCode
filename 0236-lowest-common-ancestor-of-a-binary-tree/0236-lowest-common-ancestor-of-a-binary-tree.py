# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Issolve(self,root,p,q):
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.Issolve(root.left,p,q)
        right = self.Issolve(root.right,p,q)
        if left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        return root                          
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.Issolve(root,p,q)

        