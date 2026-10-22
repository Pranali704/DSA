class Node:
 def __init__(self, data):
 self.data = data # store data
 self.next = None # store reference to next node
# Linked List class
class LinkedList:
 def __init__(self):
 self.head = None # initially empty list
 # Insert at the end
 def append(self, data):
 new_node = Node(data)
 if self.head is None: # if list is empty
 self.head = new_node
 return
 last = self.head
 while last.next: # traverse to the end
 last = last.next
 last.next = new_node
# Print the list
 def print_list(self):
 current = self.head
 while current:
 print(current.data, end=" -> ")
 current = current.next
 print("None")
# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll. print_list()