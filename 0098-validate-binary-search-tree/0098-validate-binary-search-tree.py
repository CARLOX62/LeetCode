# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,result):
        if root is None:
            return 
        self.solve(root.left,result)
        result.append(root.val) 
        self.solve(root.right,result)   
    def isValidBST(self, root: TreeNode | None) -> bool:
        result = []

        self.solve(root,result)

        for i in range(1,len(result)):
            if result[i] <= result[i-1]:
                return False
        return True   