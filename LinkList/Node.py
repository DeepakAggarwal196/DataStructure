'''
Created on 05-Jan-2017

@author: Aggarwal
'''
class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        
    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self) 