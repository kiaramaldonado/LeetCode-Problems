# Given a binary tree, determine if it is hieght balanced.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0  # height is 0

            left = check(node.left)
            if left == -1:
                return -1  # not balanced

            right = check(node.right)
            if right == -1:
                return -1  # not balanced

            if abs(left - right) > 1:
                return -1  # not balanced

            return max(left, right) + 1  # height of subtree

        return check(root) != -1
        