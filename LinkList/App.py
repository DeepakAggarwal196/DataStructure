'''
Created on 05-Jan-2017

@author: Aggarwal
'''
from LinkList.LinkedList import LinkedList

linkedList = LinkedList()

linkedList.insertStart(12)
linkedList.insertEnd(15)
linkedList.insertStart(8)
linkedList.insertEnd(52)
linkedList.insertEnd(41)

linkedList.traverse()
print("size is {} \n".format(linkedList.size()))

linkedList.remove(15)
linkedList.remove(8)
linkedList.remove(52)

linkedList.traverse()
print("size is {} \n".format(linkedList.size()))