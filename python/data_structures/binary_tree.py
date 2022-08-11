class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        # initialization here
        self.root = None

    def add(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return

    def pre_order(self):
        def walk(root, value):
            if root is None:
                return
            value.append(root.value)
            walk(root.left, value)
            walk(root.right, value)

        ordered = []
        walk(self.root, ordered)
        return ordered

    def in_order(self):
        def walk(root, value):
            if root is None:
                return
            walk(root.left, value)
            value.append(root.value)
            walk(root.right, value)

        ordered = []
        walk(self.root, ordered)
        return ordered

    def post_order(self):
        def walk(root, value):
            if root is None:
                return
            walk(root.left, value)
            walk(root.right, value)
            value.append(root.value)

        ordered = []
        walk(self.root, ordered)
        return ordered

    def find_maximum_value(self):
        # Base case
        if self.root is None:
            return

        def walk(root):
            if root is None:
                return
            if root.value > max:
                max = root.value
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return max

        # return max
        # print('')
