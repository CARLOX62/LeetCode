# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root,result):
        if root == None:
            return
        self.postorder(root.left,result)
        self.postorder(root.right,result)
        result.append(root.val)    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        self.postorder(root,result)

        return result