class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next

if __name__ == "__main__":
    n = int(input("Total no of Nodes to enter: "))
    
    if n == 0:
        print("The list is empty.")
        head = None
    else:
        data = int(input(f"Enter data for node 1: "))
        head = SinglyLinkedListNode(data)
        current = head
        
        for i in range(2, n + 1):
            data = int(input(f"Enter data for node {i}: "))
            new_node = SinglyLinkedListNode(data)
            current.next = new_node
            current = new_node

    print("\nLinked list data:")
    printLinkedList(head)
