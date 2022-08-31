from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable
import pytest


def tree_intersection(tree_a, tree_b):
    match = set()
    hashtable = Hashtable()
    tree_a_value = BinaryTree.pre_order(tree_a)
    tree_b_value = BinaryTree.pre_order(tree_b)

    for num in tree_a_value:
        hashtable.set(num, num)

    for num in tree_b_value:
        if hashtable.contains(num):
            match.add(num)

    return match


