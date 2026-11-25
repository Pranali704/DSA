#Q. 1 E-Commerce Product Search System
# An e-commerce company maintains product IDs in a BST to enable efficient
# product searching.
# Tasks:
# 1. Create a BST using product IDs.
# Insert the following product IDs:
# 150, 100, 200, 75, 125, 175, 250, 60, 90, 110.
# 2. Display product IDs in ascending order.
# 3. Search for product ID 175 exists.
# 4. Delete product ID 100.
# 5. Display the BST using inorder, preorder, and postorder traversals.
# 6. Find the minimum and maximum product IDs.

# Q. 1 E-Commerce Product Search System

class Node:
    def __init__(self, value):
        self.pid = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.pid < temp.pid:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def inorder(self, rt):
        if rt is not None:
            self.inorder(rt.left)
            print(rt.pid, end=" ")
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt is not None:
            print(rt.pid, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self, rt):
        if rt is not None:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.pid, end=" ")

    def search(self, key):
        temp = self.root

        while temp:
            if temp.pid == key:
                return True
            elif key < temp.pid:
                temp = temp.left
            else:
                temp = temp.right

        return False

    def min_max(self, rt):
        if rt is None:
            return

        temp = rt

        while temp.left is not None:
            temp = temp.left

        print("\nMin value:", temp.pid)

        temp = rt

        while temp.right is not None:
            temp = temp.right

        print("Max value:", temp.pid)

    def del_node(self, rt, val):
        if rt is None:
            return None

        if val < rt.pid:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.pid:
            rt.right = self.del_node(rt.right, val)

        else:
            if rt.left is None:
                return rt.right

            if rt.right is None:
                return rt.left

            succ = self.get_successor(rt)
            rt.pid = succ.pid
            rt.right = self.del_node(rt.right, succ.pid)

        return rt

    def get_successor(self, temp):
        temp = temp.right

        while temp is not None and temp.left is not None:
            temp = temp.left

        return temp


b1 = BST()

# Insert product IDs
b1.insert(Node(150))
b1.insert(Node(100))
b1.insert(Node(200))
b1.insert(Node(75))
b1.insert(Node(125))
b1.insert(Node(175))
b1.insert(Node(250))
b1.insert(Node(60))
b1.insert(Node(90))
b1.insert(Node(110))

print("\nProduct ID in ascending order:")
b1.inorder(b1.root)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

print("\nInorder:")
b1.inorder(b1.root)

# Find minimum and maximum
b1.min_max(b1.root)

# Delete product ID 100
b1.root = b1.del_node(b1.root, 100)

print("\nAfter deleting 100:")
b1.inorder(b1.root)

# Search product ID 175
if b1.search(175):
    print("\nFound the node with value 175")
else:
    print("\nNot found")



