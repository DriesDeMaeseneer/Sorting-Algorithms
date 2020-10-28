#!/bin/python3

from BinTree import NTree,treenode

def TreeSort(array):
    # Declade A a binary tree from lib BinTree
    a = NTree()
    # All items will be inserted into a binary tree.

    for i in array:
        a.insert(treenode(i))
