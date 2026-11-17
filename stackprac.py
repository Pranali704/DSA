
stack = []

def push(x):
    stack.append(x)
    print("Element pushed:", x)

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

def reverse_string(s):
    temp = []

    for ch in s:
        temp.append(ch)

    rev = ""

    while len(temp) > 0:
        rev = rev + temp.pop()

    print("Reversed String:", rev)

def reverse_stack():
    temp = []

    while len(stack) > 0:
        temp.append(stack.pop())

    while len(temp) > 0:
        stack.append(temp.pop())

    print("Reversed Stack:", stack)


push(10)
push(20)
push(30)

pop()
display()

reverse_string("PYTHON")

reverse_stack()
