from BinarySearchTree import BinarySearchTree

def main():
    tree = BinarySearchTree()
    tree.insertNode(10)
    tree.insertNode(5)
    tree.insertNode(15)
    tree.insertNode(3)
    tree.insertNode(7)
    tree.insertNode(12)
    tree.insertNode(17)
    tree.insertNode(1)
    tree.insertNode(4)
    tree.insertNode(6)
    tree.insertNode(8)
    tree.insertNode(11)
    tree.insertNode(13)
    tree.insertNode(16)
    tree.insertNode(18)
    tree.printTree()
    print(tree.searchNode(10))
    print(tree.searchNode(2))
    print(tree.searchNode(15))

if __name__ == "__main__":
    main()