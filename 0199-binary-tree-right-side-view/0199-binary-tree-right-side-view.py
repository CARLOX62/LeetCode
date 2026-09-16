# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        def reversepostorder(root,level,ans):
            if root is None:
                return
            if len(ans) == level:
                ans.append(root.val)
            if root.right:
                reversepostorder(root.right,level+1,ans)
            if root.left:
                reversepostorder(root.left,level+1,ans)
        ans = []
        reversepostorder(root,0,ans)
        return ans
            