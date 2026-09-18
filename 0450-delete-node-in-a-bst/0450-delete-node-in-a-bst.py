# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None
        if root.val == key:
            return self.deletion(root)
        temp = root
        while temp is not None:
            if temp.val > key:
                if temp.left is not None and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is not None and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right
        return root

    def deletion(self,node:TreeNode):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            right_child = node.right
            last_right = self.findlastRight(node.left)
            last_right.right = right_child
            return node.left
    def findlastRight(self,node:TreeNode):
        while node.right is not None:
            node = node.right
        return node            
