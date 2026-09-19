# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        if root == None:
            return

        # Go to left subtree
        self.solve(root.left, k)

        # Visit current node
        self.count += 1

        # Check if current node is kth smallest
        if self.count == k:
            self.answer = root.val
            return

        # Go to right subtree
        self.solve(root.right, k)   
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:    
        self.count = 0
        self.answer = 0

        self.solve(root, k)

        return self.answer