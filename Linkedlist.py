#singly linear linked list

class Node:
    def __init__(self, val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None #here null = none
    def append(self, new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node #appending new_node
    def print(self):
        count=0
        sum = 0


        temp=self.head

        while temp:
            count=count+1 #similar to this do of sum
            #sum of all positive nodes
            if temp.data > 0:
                sum = sum + temp.data

            print(temp.data)
            temp = temp.next
        print(sum)
        print(count)

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.print()




