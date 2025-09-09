from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PreOrder(root):
    if root is None:
        return
    print(root.data, end=' ')
    PreOrder(root.left)
    PreOrder(root.right)

def build_tree(nodes):
    if not nodes or nodes[0] == -1:
        return None

    root = Node(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        current = queue.popleft()
        if i < len(nodes) and nodes[i] != -1:
            current.left = Node(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] != -1:
            current.right = Node(nodes[i])
            queue.append(current.right)
        i += 1

    return root

if __name__ == "__main__":
    arr = list(map(int, input("Enter tree nodes in level order (-1 for no node): ").split()))
    root = build_tree(arr)
    print("Preorder traversal:")
    PreOrder(root)
    print()
