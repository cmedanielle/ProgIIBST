from bst import BST

arvore = BST()

arvore.insert(30)
arvore.insert(23)
arvore.insert(7)
arvore.insert(28)
arvore.insert(70)
arvore.insert(89)
arvore.insert(26)

arvore.inOrderTransversal()

arvore.remove(30, arvore.root)
print()
arvore.inOrderTransversal()