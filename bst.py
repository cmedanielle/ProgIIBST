class BST:
    def __init__(self):
        # inicializa uma árvore vazia
        self.root = None

    # verifica se a árvore está vazia ou não
    def isEmpty(self):
        return self.root is None
        # if self.root == None:
        #     return True
        # return False

    # cria um nó de uma árvore genérica
    # def createNode(self, data, left = None, right = None):
    #     return TreeNode(data, left, right)

    # insere um valor em uma árvore binária de busca
    def insert(self, key):
        if self.isEmpty():
            # se a árvore estiver vazia, o novo nó será a raíz
            self.root = TreeNode(key)
        else:
            # caso contrário, é preciso buscar o local correto de inserção do novo nó recursivamente
            self._insert(key, self.root)

            # função auxiliar para inserir recursivamente um valor em uma árvore binária de busca
    def _insert(self, key, root):
        if root is None:
            return TreeNode(key)
        elif key < root.data:
            root.left = self._insert(key, root.left)
        elif key > root.data:
            root.right = self._insert(key, root.right)
        return root

    # verifica qual o maior valor contido em uma subárvore
    def maxValue(self, root):
        if root is None:
            return None
        if root.right is not None:
            return self.maxValue(root.right)
        return root.data

    # verifica qual o menor valor contido em uma subárvore
    def minValue(self):
        return self._minValue(self.root)

    # verifica qual o menor valor contido em uma subárvore (recursivamente)
    def _minValue(self, root):
        if root is None:
            return None
        if root.left is not None:
            return self._minValue(root.left)
        return root.data

    # remove um nó de uma árvore binária de busca
    def remove(self, key, root):
        # chave não existe na árvore
        if root is None:
            return None
        # busca pelo nó, caso a chave exista
        elif key < root.data:
            root.left = self.remove(key, root.left)
            return root
        elif key > root.data:
            root.right = self.remove(key, root.right)
            return root
        else:
            # caso 1: remoção de nó folha
            if (root.right is None) and (root.left is None):
                return None
            # caso 2: remoção de nó que possui apenas um filho
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # caso 3: remoção de nó que possui ambos os filhos
            else:
                valorMinimo = self._minValue(root.right)
                root.data = valorMinimo
                root.right = self.remove(valorMinimo, root.right)
                return root

    # calcula a altura de uma árvore
    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    # atribui um determinado nó à raíz da árvore
    def setRoot(self, root):
        if self.isEmpty():
            self.root = root

            # encamihamento em pré ordem
    def preOrderTransversal(self):
        if not self.isEmpty():
            self._preOrderTransversal(self.root)

    def _preOrderTransversal(self, root):
        if root is not None:
            print(root.data, end = ' ')
            self.preOrderTransversal(root.left)
            self.preOrderTransversal(root.right)

            # encamihamento em ordem
    def inOrderTransversal(self):
        if not self.isEmpty():
            self._inOrderTransversal(self.root)

    def _inOrderTransversal(self, root):
        if root is not None:
            self._inOrderTransversal(root.left)
            print(root.data, end = ' ')
            self._inOrderTransversal(root.right)

            # encamihamento em pós ordem
    def postOrderTransversal(self):
        if not self.isEmpty():
            self._postOrderTransversal(self.root)

    def _postOrderTransversal(self, root):
        if root is not None:
            self._postOrderTransversal(root.left)
            self._postOrderTransversal(root.right)
            print(root.data, end = ' ')

    # calcula a soma dos valores armazenados nos nós de uma árvore
    def sumTree(self, root):
        pass

    # calcula o total de números pares armazenados em uma árvore
    def totalEvenKeys(self, root):
        pass

    # calcula o total de números ímpares armazenados em uma árvore
    def totalOddKeys(self, root):
        pass

    # dado um determinado valor, calcula o total de números
    # armazenados em uma árvore que são maiores que este valor
    def totalGreaterThan(self, key, root):
        pass

    # dado um determinado valor, calcula o total de números
    # armazenados em uma árvore que são menores que este valor
    def totalLessThan(self, key, root):
        pass

# classe auxiliar para criação de nós de uma árvore binária
class TreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right