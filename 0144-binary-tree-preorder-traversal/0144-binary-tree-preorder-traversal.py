# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        """
        Preorder Traversal:
        Root -> Left -> Right

        Uses Morris Traversal.

        Main idea:
        - No recursion
        - No stack
        - Use temporary links to come back to a node
        - Remove the temporary links after use

        Time:  O(n)
        Space: O(1)
        """

        result = []
        current = root

        while current is not None:

            # CASE 1:
            # Current has NO left child.
            #
            # We can directly visit current
            # and then move to the right.
            if current.left is None:
                result.append(current.val)

                # Move to right subtree
                current = current.right

            else:
                # CASE 2:
                # Current has a left subtree.

                # Find the inorder predecessor:
                # rightmost node of current's left subtree.
                predecessor = current.left

                # Move to the rightmost node.
                #
                # Stop when:
                # 1. predecessor.right == None
                #    -> Temporary link needs to be created.
                #
                # 2. predecessor.right == current
                #    -> Temporary link already exists.
                while (predecessor.right is not None and
                       predecessor.right != current):

                    predecessor = predecessor.right

                # CASE 2A:
                # Temporary link does not exist.
                if predecessor.right is None:

                    # PREORDER:
                    # Visit current BEFORE going to left subtree.
                    result.append(current.val)

                    # Create temporary link:
                    #
                    # predecessor -> current
                    #
                    # This helps us return to current
                    # after finishing the left subtree.
                    predecessor.right = current

                    # Move to left subtree
                    current = current.left

                else:
                    # CASE 2B:
                    # Temporary link already exists.
                    #
                    # Left subtree is completely processed.

                    # Remove temporary link
                    # and restore original tree.
                    predecessor.right = None

                    # Move to right subtree
                    current = current.right

        return result