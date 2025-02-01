from Node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insertNode(self, data):
        self.root = self.__insertNode(self.root, data)
        
    def __insertNode(self,currentNode, data):
        if currentNode is None:
            return Node(data)
        if data < currentNode.data:
            currentNode.left = self.__insertNode(currentNode.left, data)
        else:
            currentNode.right = self.__insertNode(currentNode.right, data)
        return currentNode

    def searchNode(self, data):
        return self.__searchNode(self.root, data)

    def __searchNode(self, currentNode, data):
        if currentNode is None:
            return False
        if currentNode.data == data:
            return True
        if data < currentNode.data:
            return self.__searchNode(currentNode.left, data)
        else:
            return self.__searchNode(currentNode.right, data)
    
    def printTree(self):
        self.__printTree(self.root)
      
    def __printTree(self, currentNode):
        if currentNode is None:
            return
        self.__printTree(currentNode.left)
        print(currentNode.data)
        self.__printTree(currentNode.right)

    