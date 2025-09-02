import sys
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
def Traverse(head,*argv):
    currentNode = head
    low = float('inf')
    value = sys.argv[1]
 
    max = 0
    a = False
    while(currentNode):
        print(currentNode.data," -> ",end="")
        if currentNode.data == value:
            a = True
        if currentNode.data>max:
            max = currentNode.data
        if currentNode.data<low:
            low = currentNode.data
        currentNode = currentNode.next
        
    return low,max,a,value

node1 = Node(7)
node2 = Node(2)
node3 = Node(3)
node4 = Node(5)
node5 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# n = int(input("Enter the number to be checked in the linked list: "))

a,m,check,value = Traverse(node1)
print("Lowest Value is : ",a)
print("Maximum Value is : ",m)
if(check):
    print(f"The value {value} is available in the linked list")
else:
    print(f"The value {value} is not available in the linked list")