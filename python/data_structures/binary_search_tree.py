from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):

    def add(self, value):

        def walk(root, new_node):
            if root is None:
                return
            if new_node.value < root.value:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        walk(self.root, new_node)

    def contains(self, value):
        def walk(root, target):
            if root.value == target:
                return True
            elif not root.right and target > root.value:
                return False
            elif not root. left and target < root.value:
                return False

            if root.value < target:
                return walk(root.right, target)
            if root.value > target:
                return walk(root.left, target)

        return walk(self.root, value)
