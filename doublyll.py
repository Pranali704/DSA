class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp = temp.next 
            temp.next = new_node
            new_node.prev = temp
        else: #First node
            self.head = new_node

    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            while(p!=pos -1 and temp.next):
                temp = temp.next
                p = p + 1 
            new_node.next = temp.next
        
            if temp.next:  #lastnode
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
    def reverse(self):
        temp = self.head
        if temp == None:
            print("List is empty")
            return 
        while temp.next:
            temp = temp.next 
        print("\nList elements in reverse order: ")
        while temp:
            print(temp.data, end = " ")
            temp = temp.prev
    def print(self):
        temp = self.head
        print("List elements: ")
        while temp:
            print(temp.data, " ")
            temp = temp.next
        while(temp):
            print(temp.data , end =" ")
            temp = temp.prev
    #def print(self):
     #   temp = self.head
list = LinkedList()
list.append(Node(12))
list.append(Node(52))
list.append(Node(22))
#list.print()

list.insert(Node(5),1)
list.insert(Node(512),2)
#list.print()
list.reverse()


    
