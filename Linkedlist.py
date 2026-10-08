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

    def del_node(self, value):
        temp=self.head
        #deleting first node
        if temp.data == value:
            self.head=self.head.next
            return
        while(temp):
            if temp.data == value: #searching value
                break
            else:                  #traverse
                prev=temp
                temp=temp.next
        if temp==None:
            print("value not there in list")
        prev.next=temp.next
        temp=None


#only one function to insert at betn,start,end
    def insert(self, new_node,pos):
        temp=self.head
        if pos==1: #inserting at first position
            new_node.next=self.head
            self.head=new_node
        else: #inserting node from second to last position
            p=1
            while(p!=pos-1 and temp.next!=None):
                p=p+1
            new_node.next=temp.next
            temp.next=new_node
            return

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
list.append(Node(55))

list.insert(Node(100),1)
list.print()
list.insert(Node(66),4)
list.print()




