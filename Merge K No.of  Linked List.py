class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n # type: ignore
            self.tail = n

def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()

def mergeTwoLists(l1, l2):
    dummy = Node(-1)
    current = dummy
    
    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1 is not None:
        current.next = l1
    if l2 is not None:
        current.next = l2

    return dummy.next

def mergeKLists(arr, k):
    while len(arr) > 1:
        l1 = arr.pop(0).head
        l2 = arr.pop(0).head
        merged = LL()
        merged.head = mergeTwoLists(l1, l2)
        arr.append(merged)
    return arr[0].head if arr else None

k = int(input("Enter the number of linked lists: "))
arr = []
for _ in range(k):
    m = LL()
    n = int(input("Enter the number of elements in the list: "))
    for _ in range(n):
        m.insert(int(input()))
    arr.append(m)

head = mergeKLists(arr, k)
printList(head)
