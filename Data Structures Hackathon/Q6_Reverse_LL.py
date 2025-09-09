class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next 
        current.next = prev     
        prev = current           
        current = next_node      
    
    return prev 


def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")

if __name__ == "__main__":
  
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)
    node1.next = node2
    node2.next = node3

    print("Original list:")
    printLinkedList(node1)

    reversed_head = reverse(node1)
    print("Reversed list:")
    printLinkedList(reversed_head)
