'''
Created on 05-Jan-2017

@author: Aggarwal
'''
from BinarySearchTreeDS.BinarySearchTree import BST

bst =BST()

bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)

bst.traverseInOrder()
print("")
print(bst.getMax())
print(bst.getMin())
print("")

bst.remove(10)
bst.traverseInOrder()
print("")
print(bst.getMax())
print(bst.getMin())
