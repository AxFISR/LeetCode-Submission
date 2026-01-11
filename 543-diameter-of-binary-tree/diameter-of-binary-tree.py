class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxres = 0  # לא כמשתנה מחלקה קבוע, אלא לכל ריצה

        def height(node):
            if node is None:
                return 0

            lefth = height(node.left)
            righth = height(node.right)

            # מעדכנים קוטר מקסימלי (במספר edges)
            self.maxres = max(self.maxres, lefth + righth)

            # מחזירים גובה
            return 1 + max(lefth, righth)

        height(root)
        return self.maxres
