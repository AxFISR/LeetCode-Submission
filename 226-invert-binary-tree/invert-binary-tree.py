class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None

        # swap
        root.left, root.right = root.right, root.left

        # recurse
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
