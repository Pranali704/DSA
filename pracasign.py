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

    def display(self):
        if self.isempty():
            print("Stack is empty...")
        else:
            print("Stack contains...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    def rev_string(self):
        s = input("Enter a string: ")
        temp = []

        for i in s:
            temp.append(i)

        rev = ""

        while len(temp) > 0:
            rev = rev + temp.pop()

        print("Reversed string:", rev)

    # Reverse stack using another stack
    def rev(self, st1):
        temp = self.top

        while temp:
            st1.push(Node(temp.data))
            temp = temp.next

        print("After reversed:")
        st1.display()


# Main program
st = Stack()
st1 = Stack()

st.push(Node(10))
st.push(Node(50))
st.push(Node(70))
st.push(Node(30))
st.push(Node(40))

print("Original Stack:")
st.display()

st.pop()
st.pop()
st.pop()

print("After pop:")
st.display()

st.rev_string()

st.rev(st1)