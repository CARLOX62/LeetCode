# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        current = root

        while current is not None:
            # CASE 1: Current has no left child
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                # CASE 2: Current has left child
                # Find the inorder predecessor
                predecessor = current.left

                # Go to the rightmost node in left subtree
                # Or find the node right child is current
                while (predecessor.right is not None and predecessor.right != current):
                    predecessor = predecessor.right

                # Make current as right child of predecessor
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    # Revert the changes: remove the right child link
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        return result                        
        