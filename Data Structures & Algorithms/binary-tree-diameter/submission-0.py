# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        if node == None:
            return 0
        l_height = self.dfs(node.left)
        r_height = self.dfs(node.right)
        self.diameter = max(l_height + r_height, self.diameter)
        return max(l_height, r_height) + 1