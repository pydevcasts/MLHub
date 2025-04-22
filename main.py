class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def to_string(self):
        node = self.head
        while node is not None:
            print(node.value)
            if type(node.value) == str:
                raise TypeError("invalid type of value ...")
            node = node.next
            if node is None:
                print("null ..")

node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)

node1.next = node2
node2.next = node3
ll = LinkedList(head=node1)
ll.to_string()

