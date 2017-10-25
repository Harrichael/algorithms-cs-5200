
import random

class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        self.insert_node(Tree(value))

    def insert_node(self, node):
        if self.data is None:
            self.data = node.data
        elif self.data > node.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert_node(node)
        elif self.data < node.data:
            if self.right is None:
                self.right = node
            else:
                self.right.insert_node(node)

    def __contains__(self, member):
        if self.data == member:
            return True
        elif member < self.data and self.left:
            return member in self.left
        elif member > self.data and self.right:
            return member in self.right
        else:
            return False

    def max(self):
        if not self.right:
            return self.data
        else:
            return self.right.max()

    def min(self):
        if not self.left:
            return self.data
        else:
            return self.left.min()

    def remove(self, value):
        if self.data == value:
            if self.left or self.right:
                if (random.randint(0, 1) and self.left) or not self.right:
                    self.data = self.left.max()
                    self.left.remove(self.data)
                else:
                    self.data = self.right.min()
                    self.right.remove(self.data)
            else:
                return True
        elif value < self.data and self.left:
            if self.left.remove(value):
                self.left = None
        elif value > self.data and self.right:
            if self.right.remove(value):
                self.right = None
        return False 

    def depth_first(self):
        yield 0, self
        if self.left:
            for depth, node in self.left.depth_first():
                yield depth + 1, node
        if self.right:
            for depth, node in self.right.depth_first():
                yield depth + 1, node


