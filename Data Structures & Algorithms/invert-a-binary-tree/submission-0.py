# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        # dfs
        self.traverse(root)

        return root

    def traverse(self, node: TreeNode):

        if node.left != None:
            self.traverse(node.left)
        if node.right != None:
            self.traverse(node.right)

        self.exchange(node)


    def exchange(self, node: TreeNode):
        tmp = node.left
        node.left = node.right
        node.right = tmp

        