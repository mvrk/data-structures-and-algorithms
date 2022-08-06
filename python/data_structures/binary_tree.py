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