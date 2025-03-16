from BinarySearchTree import BinarySearchTree

def main():
    tree = BinarySearchTree()
    tree.insertNode('Carlos')
    tree.insertNode('Karen')
    tree.insertNode('Zuriel')
    tree.insertNode('Daniel')
    tree.insertNode('Valeria')
    print(tree.searchNode('Karen'))
    print(tree.searchNode('Manuel'))
    print(tree.searchNode('Zuriel'))

if __name__ == "__main__":
    main()