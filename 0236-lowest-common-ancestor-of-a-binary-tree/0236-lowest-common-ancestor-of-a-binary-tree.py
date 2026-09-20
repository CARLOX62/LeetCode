# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Issolve(self,root,target,path):
        if root is None:
            return False
        path.append(root)    

        if root == target:
            return True
        if self.Issolve(root.left,target,path) or self.Issolve(root.right,target,path):
            return True
        path.pop()
        return False        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []

        self.Issolve(root,p,path1)
        self.Issolve(root,q,path2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1

        return path1[i - 1]