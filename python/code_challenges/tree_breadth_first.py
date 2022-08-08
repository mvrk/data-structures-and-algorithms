from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    queue = Queue()
    node = []

    if not tree:  # empty tree
        return node
    if not tree.root:  # tree only have one node
        return node
    if not queue.front:  # queue is empty
        queue.enqueue(tree.root)
    while queue.front:
        root = queue.dequeue()
        node.append(root.value)
        if root.left:
            queue.enqueue(root.left)
        if root.right:
            queue.enqueue(root.right)
    return node
