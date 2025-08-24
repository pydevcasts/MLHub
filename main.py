# class Node:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next


# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head
    
#     def to_string(self):
#         node = self.head
#         while node is not None:
#             print(node.value, end = " -> ")
#             if type(node.value) == str:
#                 raise TypeError("invalid type of value ...")
#             node = node.next
#             if node is None:
#                 print("null ..")

# node1 = Node(value=1)
# node2 = Node(value=2)
# node3 = Node(value=3)

# node1.next = node2
# node2.next = node3
# ll = LinkedList(head=node1)
# ll.to_string()

# # class Node:
# #     def __init__(self, data):
# #         self.data = data #data node
# #         self.next = None #pointer to next node


# # class LinkedList:
# #     def __init__(self):
# #         self.head = None #head of list
    
# #     def append(self, data):
# #         new_node = Node(data) #create new node
# #         if self.head is None: 
# #             self.head=new_node 
# #         else:
     
# #             current =  self.head
# #             while current.next:
# #                 current = current.next
# #             current.next = new_node

# #     def print_list(self):
# #         current =self.head
# #         while current:
# #             print(current.data, end = " -> ")
# #             current= current.next
# #         print("None")

# # ll = LinkedList()
# # ll.append(10)
# # ll.append(20)
# # ll.append(30)
# # ll.print_list()

# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)
    
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         return None
#     def front(self):
#         if not self.is_empty():
#             return self.items[0]
        
#     def is_empty(self):
#         return len(self.items) == 0
    
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.front())
# print(q.is_empty())


# x = "hello, how"

# p= x.split(",")
# print(len(p))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot] #logn
    mid = [i for i in arr if i == pivot] #n
    right = [i for i in arr if i > pivot] #logn
    return quick_sort(left) + mid +  quick_sort(right)
print(quick_sort([34,7,23,32,5,62]))
