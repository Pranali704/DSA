class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, newnode):
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.isempty():
            print("Stack is empty....")
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp
        #return popped return to reverse 


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    # Enqueue
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    # Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Deleted node:", temp.data)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # Display
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end="->")
                temp = temp.next
            print()

    # Reverse queue using stack
    def rev(self, st):
        temp = self.front

        while temp:
            st.push(Node(temp.data))
            temp = temp.next

        temp = self.front

        while not st.isempty():
            temp.data = st.pop().data
            temp = temp.next
    def rev_stack(s1):
        q1=LQueue()
        while not s1.isempty():
            q1.enqueue(Node(s1.pop()))
        q1.print()

    

    # Merge two queues
    def merge(self, que2):
        temp = que2.front

        while temp:
            self.enqueue(Node(temp.data))
            temp = temp.next

    # Check identical queues
    def identical(self, que2):
        temp1 = self.front
        temp2 = que2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                print("Queues are not identical")
                return

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            print("Queues are identical")
        else:
            print("Queues are not identical")
    


# Main program
que = LQueue()
que2 = LQueue()
st = Stack()

# First Queue
que.enqueue(Node(12))
que.enqueue(Node(72))
que.enqueue(Node(56))
que.enqueue(Node(20))
que.enqueue(Node(17))

print("Display first queue:")
que.display()

# Second Queue
que2.enqueue(Node(22))
que2.enqueue(Node(55))
que2.enqueue(Node(54))
que2.enqueue(Node(46))
que2.enqueue(Node(13))

print("Display second queue:")
que2.display()

# Dequeue
que.dequeue()
que.dequeue()
que.dequeue()

print("Display queue after dequeue:")
que.display()

# Reverse Queue
que.rev(st)

print("Reversed Queue:")
que.display()

# Merge Queues
que.merge(que2)

print("After merging:")
que.display()

# Check identical queues
que.identical(que2)
#reverse_stack(st)
