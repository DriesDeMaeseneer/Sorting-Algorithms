#!/bin/python3

from BinTree import NTree,treenode

def TreeSort(array):
    # Declade A a binary tree from lib BinTree
    a = NTree()
    # All items will be inserted into a binary tree.

    for i in array:
    # insert all the items into the tree, one by one.
        a.insert(treenode(i))
    # call the method inorder() in lib BinTree to print out the sorted version
    a.inorder()
