# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:    
        count = 0
        curr = root

        while curr:
            # If there is no left subtree
            if curr.left is None:
                count += 1

                if count == k:
                    return curr.val

                curr = curr.right

            else:
                # Find inorder predecessor
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right

                # Create a temporary link
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left

                # Remove temporary link
                else:
                    pred.right = None

                    count += 1

                    if count == k:
                        return curr.val

                    curr = curr.right