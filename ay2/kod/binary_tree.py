#Binary Tree, her düğümün en fazla iki çocuğunun olduğu bir veri yapısıdır.
#Bu kodda küçük değerleri sola, büyük veya eşit değerleri sağa ekleyerek ağacı oluşturuyorum.
#inorder, preorder ve postorder ise ağacı farklı sıralamalarla dolaşmamı sağlıyor.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Yeni node ekleme
    def insert(self, data):

        yeni_node = TreeNode(data)

        # Ağaç boşsa yeni node root olur
        if self.root is None:
            self.root = yeni_node
            return

        simdiki = self.root

        while True:

            # Küçük değerler sola gider
            if data < simdiki.data:

                if simdiki.left is None:
                    simdiki.left = yeni_node
                    return

                simdiki = simdiki.left

            # Büyük veya eşit değerler sağa gider
            else:

                if simdiki.right is None:
                    simdiki.right = yeni_node
                    return

                simdiki = simdiki.right

    # Inorder: Sol - Kök - Sağ
    def inorder(self, node):

        if node is None:
            return

        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    # Preorder: Kök - Sol - Sağ
    def preorder(self, node):

        if node is None:
            return

        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    # Postorder: Sol - Sağ - Kök
    def postorder(self, node):

        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)


tree = BinaryTree()

tree.insert(9)
tree.insert(6)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(35)

print("Inorder:")
tree.inorder(tree.root)

print("\nPreorder:")
tree.preorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)

