# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None  #next node is null
class LinkedList:
    def __init__(self):
        self.head = None #Head initialization
    # Add new node
    def addNode(self, node):
        new_Node = ListNode(node)

        if self.head is None:
            self.head = new_Node # If head is empty assign new head
            return
        last = self.head # last is head
        while last.next:
            last = last.next
        
        last.next = new_Node
    # Print function for linked list
    def display(self):
        temp = self.head
 
        while temp:
            print(temp.val, end = " ")
            temp = temp.next

# Remove nth Node
def removeNode(head, n):
    # Using 2 pointers
    first = head
    second = head
    count = 1
    while count <= n:
        second = second.next
        count += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next

lst = []
# number of elements as input
totalNode = int(input("Enter number of elements (1-30) : "))
if totalNode in range (1,31): # First Contraint 1<= sz <= 30
    for i in range(0, totalNode):
        ele = int(input("Enter number 0-100: "))
        if ele in range (0, 101):
            lst.append(ele) # adding the element

        else:
            print ('Node val out of range')
            break
        print(lst)
       
    
else: print ("sz out of range")

# Enter the node value to remove
nth = int(input("Enter node to be removed: "))
ll = LinkedList()
for i in lst:
    ll.addNode(i)

print("Linked list: ");
ll.display()
removeNode (ll.head, nth)
print("\nLinked list after removing nth Node: ");
ll.display()