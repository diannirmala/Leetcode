# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        # hitung kedalaman kiri
        left_depth = self.getDepth(root.left)
        # hitung kedalaman kanan
        right_depth = self.getDepth(root.right)
        
        if left_depth == right_depth:
            # subtree kiri adalah full tree
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # subtree kanan adalah full tree
            return (1 << right_depth) + self.countNodes(root.left)
    
    def getDepth(self, node):
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth


# === Contoh penggunaan ===
if __name__ == "__main__":
    # bikin tree: 
    #       1
    #      / \
    #     2   3
    #    / \  /
    #   4  5 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()
    print("Jumlah node:", sol.countNodes(root))  # harusnya 6
