# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root != None and subRoot != None:
            return  self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
    def isSameTree(self, root_equal, subroot_equal):
        if root_equal == None and subroot_equal == None:
            return True
        if root_equal == None or subroot_equal == None:
            return False
        if root_equal.val != subroot_equal.val:
            return False
        return self.isSameTree(root_equal.left,subroot_equal.left) and self.isSameTree(root_equal.right,subroot_equal.right)
