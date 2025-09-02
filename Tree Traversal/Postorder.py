class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end = " ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print("Postorder Traversal:")
Postorder(root)
