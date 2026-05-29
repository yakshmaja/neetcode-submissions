# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, node):
        if not node:
            return "null"

        return "^" + str(node.val) + \
               self.preorder(node.left) + \
               self.preorder(node.right)

    def isSubtree(self, root, subRoot):
        full_tree = self.preorder(root)
        sub_tree = self.preorder(subRoot)

        return sub_tree in full_tree