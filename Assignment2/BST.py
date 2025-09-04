class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(root, value):
            if not root:
                return False
            if value == root.value:
                return True
            elif value < root.value:
                return _search(root.left, value)
            else:
                return _search(root.right, value)

        return _search(self.root, value)

    def inorder(self):
        def _inorder(root):
            if root:
                _inorder(root.left)
                print(root.value, end=" ")
                _inorder(root.right)

        _inorder(self.root)
        print()

    def preorder(self):
        def _preorder(root):
            if root:
                print(root.value, end=" ")
                _preorder(root.left)
                _preorder(root.right)

        _preorder(self.root)
        print()

    def postorder(self):
        def _postorder(root):
            if root:
                _postorder(root.left)
                _postorder(root.right)
                print(root.value, end=" ")

        _postorder(self.root)
        print()


bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)

print("Inorder traversal:")
bst.inorder()       

print("Preorder traversal:")
bst.preorder()     

print("Postorder traversal:")
bst.postorder()     

print("Search 60:", bst.search(60))       
print("Search 90:", bst.search(90))        

