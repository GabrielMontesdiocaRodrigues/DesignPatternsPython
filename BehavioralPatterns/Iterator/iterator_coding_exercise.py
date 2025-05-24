class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        def traverse(current):
            yield current
            if current.left:
                for left in traverse(current.left):
                    yield left
            if current.right:
                for right in traverse(current.right):
                    yield right
        for node in traverse(self):
            yield node.value


if __name__ == '__main__':
    root = Node("A", Node("B", Node("D"), Node("E")), Node("C", Node("F")))

    for x in root.traverse_preorder():
        print(x)
